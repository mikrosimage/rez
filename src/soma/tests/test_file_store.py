from rez.tests.util import TestBase, TempdirMixin
import rez.vendor.unittest2 as unittest
from soma.file_store import FileStore
import time
import os


class TestFileStore(TestBase, TempdirMixin):
    @classmethod
    def setUpClass(cls):
        TempdirMixin.setUpClass()
        cls.settings = {}

    @classmethod
    def tearDownClass(cls):
        TempdirMixin.tearDownClass()

    def test_1(self):
        store = FileStore(self.root)

        def _wait():
            time.sleep(1.1)  # git only has one-second resolution on commits

        def _write(filename, txt):
            _wait()
            filepath = os.path.join(self.root, filename)
            with open(filepath, 'w') as f:
                f.write(txt)
            store.update(filename)

        def _del(filename):
            _wait()
            filepath = os.path.join(self.root, filename)
            os.remove(filepath)
            store.update(filename)

        self.assertEqual(store.read("foo"), None)
        t1 = time.time()
        _write("foo", "hello")
        self.assertEqual(store.read("foo"), "hello")
        t2 = time.time()
        _write("foo", "greetings")
        _write("bah", "hey")
        self.assertEqual(store.read("foo"), "greetings")
        t3 = time.time()
        _del("foo")
        self.assertEqual(store.read("foo"), None)
        t4 = time.time()
        _write("foo", "I'm back!")
        self.assertEqual(store.read("foo"), "I'm back!")
        t5 = time.time()

        self.assertEqual(store.read("foo", t1), None)
        self.assertEqual(store.read("foo", t2), "hello")
        self.assertEqual(store.read("foo", t3), "greetings")
        self.assertEqual(store.read("foo", t4), None)
        self.assertEqual(store.read("foo", t5), "I'm back!")

        self.assertEqual(set(store.filenames(t1)), set())
        self.assertEqual(set(store.filenames(t2)), set(["foo"]))
        self.assertEqual(set(store.filenames(t3)), set(["foo", "bah"]))
        self.assertEqual(set(store.filenames(t4)), set(["bah"]))
        self.assertEqual(set(store.filenames(t5)), set(["foo", "bah"]))


def get_test_suites():
    suites = []
    suite = unittest.TestSuite()
    suite.addTest(TestFileStore("test_1"))
    suites.append(suite)
    return suites


if __name__ == '__main__':
    unittest.main()

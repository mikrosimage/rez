name = 'rez'
version = 'mikros2.4.1'

requires = ['python-2.7'] # for logging

def commands():
    env.PYTHONPATH.append('{root}/src')
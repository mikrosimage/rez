name = 'rez'
version = 'rc.2.0.0.mikros.2.0'

requires = ['python-2.7'] # for logging

def commands():
    env.PYTHONPATH.append('{root}/src')


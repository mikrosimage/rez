name = 'rez'
version = 'rc.mikros2.6.0'

requires = ['python-2.7'] # for logging

def commands():
    env.PYTHONPATH.append('{root}/src')

#    env.PATH.append('{root}/bin')

name = 'rez'
version = '2.0.0.mikros.4.0'

requires = ['python-2.7'] # for logging

custom = {
    "authors": ['nerdvegas'],
    "maintainers": ["coreTech"]
}

def commands():
    env.PYTHONPATH.append('{root}/src')
    env.PYTHONPATH.append('/s/apps/lin/rezRoot/current/python')


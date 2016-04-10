import sys
from setuptools import setup

if sys.argv[-1] == 'setup.py':
    print('To install, run \'python setup.py install\'')
    print()

sys.path.insert(0, 'sports_naarad')

if __name__ == "__main__":
    setup(
        name = 'sport-naarad',
        version = '0.1',
        author = 'pyrag-groups',
        author_email = 'utkarsh.gupta550@gmail.com',
        description = 'Get latest updates for football and cricket on command-line',
        url='',
        keywords='sports-naarad is a command line tool to get updates for football and cricket',
        packages = ['sports_naarad', 'sports_naarad.extern'],
        license = 'MIT License',
        entry_points = {
            'console_scripts': [
            'sports-naarad = sports_naarad.naarad:main',
            ]
        },
        install_requires = ['beautifulsoup4', 'requests',
                            'python-dateutil', 'parsedatetime']
    )

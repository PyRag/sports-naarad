import sys
from setuptools import setup

if sys.argv[-1] == 'setup.py':
    print('To install, run \'python setup.py install\'')
    print()

sys.path.insert(0, 'pyrag')

if __name__ == "__main__":
    setup(
        name = 'pyrag',
        version = '0.1',
        author = 'pyrag-groups',
        author_email = 'utkarsh.gupta550@gmail.com',
        description = 'Get latest updates for football and cricket on command-line',
        url='https://github.com/npcoder2k14/HackInTheNorth-PYRAG',
        keywords='pyrag is a command line tool to get updates for football and cricket',
        packages = ['pyrag_sports', 'pyrag_sports.extern'],
        license = 'MIT License',
        entry_points = {
            'console_scripts': [
            'pyrag = pyrag_sports.pyrag:main',
            ]
        },
        install_requires = ['beautifulsoup4', 'requests',
                            'python-dateutil', 'parsedatetime']
    )

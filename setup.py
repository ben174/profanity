from distutils.core import setup

setup(
    name='profanity',
    version='1.0',
    packages=['profanity',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description='''A module to discover (and clean) profanity in strings.
    '''
    ,
    data_files=[('data', ['profanity/data/wordlist.txt']),], 
    package_data = {
        '': ['*.txt', 'data/wordlist.txt' ],
    },
    include_package_data = True, 
    entry_points={
        'console_scripts': 
        ['profanity=profanity:main'],
    }
)

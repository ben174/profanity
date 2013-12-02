"""profanity
=========

A Python library to check for (and clean) profanity in strings.

##Installation
    pip install profanity


##Usage
    from profanity import profanity
    profanity.contains_profanity("You smell like shit.")
    Out: True

    profanity.censor("You smell like shit.")
    Out: 'You smell like !@#$.'

## Features

* Load your own wordlist, or use the bundled one.
* Censors words using standard censor characters (!@#$%), or load your own
censor characters.
* Uses a pool of censor characters to create a more natural censor string.
* Censors all instances of a given word with the same censor string - for
easy correlation.

### I love Forks, Pull Requests, and Bugs!

I wrote this to satisfy my needs. Please feel free to contribute if you have
other needs that you think others would benefit from!

Feel free to contact me: http://www.bugben.com
"""

from distutils.core import setup

import profanity

try:
    from setuptools import setup
    setup   # make pep8 happy
except ImportError:
    from distutils.core import setup

setup(
    name='profanity',
    version=profanity.__version__,
    author='Ben Friedland',
    author_email='ben174@gmail.com',
    packages=['profanity'],
    url='https://github.com/ben174/profanity',
    description=profanity.__doc__,
    long_description=__doc__,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',),
    data_files=[('data', ['profanity/data/wordlist.txt']), ],
    package_data={
        '': ['profanity/data/wordlist.txt'],
    },
    include_package_data=True,
    entry_points={
        'console_scripts':
        ['profanity=profanity:main'],
    }
)

profanity
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
* Censors words using standard censor characters (!@#$%), or load your own censor characters. 
* Uses a pool of censor characters to create a more natural censor string. 
* Censors all instances of a given word with the same censor string - for easy correlation.

### I love Forks, Pull Requests, and Bugs!

I wrote this to satisfy my needs. Please feel free to contribute if you have other needs that you think others would benefit from! 

Feel free to contact me: http://www.bugben.com

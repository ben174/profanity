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
    Out: 'You smell like ****.'

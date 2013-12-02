#!/usr/bin/env python

import os
import argparse
import random

lines = None
words = None
_censor_chars = '@#$%!'

_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_data(path):
    return os.path.join(_ROOT, 'data', path)


def get_words():
    if not words:
        load_words()
    return words


def set_censor_characters(censor_chars):
    """ Sets the pool of censor characters. Input should be a single string
    containing all the censor charcters you'd like to use. 
    Example: "@#$%^"

    """
    _censor_chars = censor_chars 


def contains_profanity(input_text):
    """Checks the input_text for any profanity and returns True if it does.
    Otherwise, returns False.
    """
    words = get_words()
    for word in words:
        if word in input_text:
            return True
    return False


def censor(input_text):
    """ Returns the input string with profanity replaced with a random string
    of characters plucked from the censor_characters pool.

    """
    ret = input_text
    words = get_words()
    for word in words:
        cen = "".join([random.choice(list(censor_chars)) for l in list(word)])
        ret = ret.replace(word, cen)
    return ret


def load_words(filename=None):
    """ Loads and caches the profanity word list. Input file (if provided)
    should be a flat text file with one profanity entry per line.

    """
    if not filename:
        filename = get_data('wordlist.txt')
    f = open(filename)
    global words
    words = f.readlines()
    words = [w.strip() for w in words if w]


def main():
    parser = argparse.ArgumentParser(description='Check input for profanity.')
    parser.add_argument('-f', '--filename', dest='path', type=str,
                        help='Path to input file to check.')
    parser.add_argument('-t', '--text', dest='text', type=str,
                        help='Text to check.')
    parser.add_argument("--censor", help="Returns censored text.",
                                action="store_true")

    args = parser.parse_args()
    if args.path:
        f = open(args.path)
        text = "".join(f.readlines())
    elif args.text:
        text = args.text
    else:
        print "No input specified."
        return

    if args.censor:
        print censor(text)
        return
    print contains_profanity(text)
    return


if __name__ == '__main__':
    main()

#!/usr/bin/env python

import os
import argparse

lines = None
words = None

_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_data(path):
    return os.path.join(_ROOT, 'data', path)


def get_words():
    if not words:
        load_words()
    return words


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
    ret = input_text
    words = get_words()
    for word in words:
        ret = ret.replace(word, '*'*len(word))
    return ret


def load_words(filename=None):
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
    args = parser.parse_args()
    if args.path:
        f = open(args.path)
        text = "".join(f.readlines())
    elif args.text:
        text = args.text
    else:
        print "No input specified."
        return
    print contains_profanity(text)


if __name__ == '__main__':
    main()

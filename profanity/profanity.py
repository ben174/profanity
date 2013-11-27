#!/usr/bin/env python

import os
import argparse

lines = None

_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_data(path):
    return os.path.join(_ROOT, 'data', path)


def contains_profanity(input_text):
    """Checks the input_text for any profanity and returns True if it does.
    Otherwise, returns False.
    """
    return False


def load_words(filename=None):
    pass

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

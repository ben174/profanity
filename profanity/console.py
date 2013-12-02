#!/usr/bin/env python

import profanity
import argparse


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
        print profanity.censor(text)
        return
    print profanity.contains_profanity(text)
    return


if __name__ == '__main__':
    main()

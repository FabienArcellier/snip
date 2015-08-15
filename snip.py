#!/usr/bin/python

import sys

def main(args):
    # case : save
    # snip save python-test
    # Create a file python-test in ~/.snip
    # that contains the content of clip board

    # case : list
    # snip list python
    # Get a list of all files that begins with
    # python

    # case : default
    # snip python-test
    # Copy the content of python-test in clipboard
    pass

if __name__ == "__main__":
    main(sys.argv[1:])
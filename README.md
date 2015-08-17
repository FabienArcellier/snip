Installation
=============

Install on linux only. It will create the script shortcut in
/usr/bin

        make install

Usage
======

        # Save the content of clipboard in
        # snippet python-test-class
        snip save python-test-class

        # List all the snippets
        snip list

        # List the snippets that begin with python
        snip list python

        # Copy the content of snippet python-test-class
        # in clipboard
        snip get python-test-class
        
        snip display python-test-class
        
        snip remove python-test-class

Setup libraries to develop
==========================

        # Install requirements.txt
        make bootstrap

To validate your code :

        # Execute pylint
        make lint

        # Execute unit test
        make tests
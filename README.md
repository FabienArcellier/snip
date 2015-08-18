Installation
=============

Install on linux only. It will create the script shortcut in
/usr/bin

        make install
        
To have access to autocomplete, source autocomplete.bash.
You can add it in your .bashrc.

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
        
Every snippets is stored in your home directory in .snip.
You can store this directory in git.

Setup libraries to develop
==========================

        # Install requirements.txt
        make bootstrap

To validate your code :

        # Execute pylint
        make lint

        # Execute unit test
        make tests
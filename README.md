Installation
=============

Clone this repository

    git clone git@github.com:FabienArcellier/snip.git

Install on ubuntu/debian.

    sudo make install

If bash_completion is installed, it will install autocomplete scripts
in /etc/bash_completion.d

Usage
======

    # Save the content of clipboard in
    # snippet python-test-class
    snip save python-test-class

    # List all the snippets
    snip list

    # List the snippets that begin by python
    snip list python

    # List and display snippets that begin by python
    snip list --display python

    # Copy the content of snippet python-test-class
    # in clipboard
    snip get python-test-class

    # Display a specific snippet
    snip display python-test-class

    # Edit a snippet
    snip edit python-test-class

    snip remove python-test-class

Every snippets is stored in your home directory in .snip.
You can store this directory in git.

Use alias with autocomplete
----------------------------

    alias ss='snip save'
    alias sg='snip get'
    alias sd='snip display'
    alias sl='snip list'

    complete -F _snip_complete_ ss
    complete -F _snip_complete_ sg
    complete -F _snip_complete_ sd
    complete -F _snip_complete_ sl

Be careful with your instanciation order in bashrc. On ubuntu,
bash_aliases is sourced before bash_completion. It won't work in this
case.


Setup libraries to develop
==========================

    # Install requirements.txt
    make bootstrap

To validate your code :

    # Execute pylint
    make lint

    # Execute unit test
    make tests

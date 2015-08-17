#!/usr/bin/python
#pylint: disable=missing-docstring

import click
import glob
import os
import pyperclip

SNIP_DIR=os.path.join(os.path.expanduser("~"), '.snip')

@click.group()
def cli():
    # case : default
    # snip python-test
    # Copy the content of python-test in clipboard
    if os.path.isdir(SNIP_DIR) == False:
        os.mkdir(SNIP_DIR)

@click.command(name='get')
@click.argument('snippet')
def get(snippet):
    # case : save
    # snip save python-test
    # Create a file python-test in ~/.snip
    # that contains the content of clip board
    with open(os.path.join(SNIP_DIR, snippet), 'rb') as f:
        content=f.read()

    pyperclip.copy(content)

@click.command(name='save')
@click.argument('snippet')
def save(snippet):
    # case : save
    # snip save python-test
    # Create a file python-test in ~/.snip
    # that contains the content of clip board
    content=pyperclip.paste()
    with open(os.path.join(SNIP_DIR, snippet), 'wb') as f:
        f.write(content)

@click.command(name='list')
@click.argument('snippetpattern', default='')
def cli_list(snippetpattern):
    # case : list
    # snip list python
    # Get a list of all files that begins with
    # python
    os.chdir(SNIP_DIR)
    files = glob.glob('{0}*'.format(snippetpattern))
    for file in files:
        print file

cli.add_command(get)
cli.add_command(save)
cli.add_command(cli_list)

if __name__ == '__main__':
    cli()

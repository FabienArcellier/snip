#!/usr/bin/python
#pylint: disable=missing-docstring

import click

@click.group(invoke_without_command=True)
@click.argument('snippet')
def cli(snippet):
    # case : default
    # snip python-test
    # Copy the content of python-test in clipboard
    click.echo('get snippet {0}'.format(snippet))

@click.command()
@click.argument('snippet')
def save(snippet):
    # case : save
    # snip save python-test
    # Create a file python-test in ~/.snip
    # that contains the content of clip board
    click.echo('save snippet {0}'.format(snippet))

@click.command(name='list')
@click.argument('snippetpattern')
def cli_list(snippetpattern):
    # case : list
    # snip list python
    # Get a list of all files that begins with
    # python
    click.echo('list snippet {0}'.format(snippetpattern))

cli.add_command(save)
cli.add_command(list)

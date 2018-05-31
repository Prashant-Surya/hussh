import click

from .commands.setup import setup
from .commands.share import share
from .commands.connect import connect

@click.group()
def cli():
    pass

cli.add_command(setup)
cli.add_command(share)
cli.add_command(connect)
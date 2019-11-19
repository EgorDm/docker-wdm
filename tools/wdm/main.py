import click

from wdm.cli import prelude

cli = click.CommandCollection(sources=[prelude])

if __name__ == '__main__':
    cli()

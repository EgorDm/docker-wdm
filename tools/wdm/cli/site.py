from wde.config import Config
from wde import container, cli

from wdm.cli import *


@prelude.command()
@click.pass_context
@pass_config
@click.argument('name', help='The name of the website')
@click.argument('type', default=None, help='community or enterprise')
@click.argument('version', default=None, help='Set the magento version being installed. Example 2.2.8')
@click.argument('options', default=None, help='add options to the composer create project commando')
def create_website(ctx, cfg: Config, name, type, version, options):
    """Creates a magneto 2 webshop with given name"""
    args = filter(None, [name, type, version, options])
    container.exec(cfg.WDE_NAME, ['create_website'] + args, require_mounted=False)
    ctx.invoke(wde.cli.secure, [name])


@prelude.command()
@click.pass_context
@pass_config
@click.argument('name', help='The name of the website')
def import_website(ctx, cfg: Config, name, ):
    """Imports magento 2 webshop with given name"""
    container.exec(cfg.WDE_NAME, ['import_website', name], require_mounted=True, cwd=cfg.DOMAIN_PATH)
    ctx.invoke(wde.cli.secure, [name])

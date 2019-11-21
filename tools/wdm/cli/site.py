from wde.config import Config
from wde import container, cli

from wdm.cli import *


@prelude.command()
@click.pass_context
@pass_config
@click.argument('name')
@click.argument('type', default=None, required=False)
@click.argument('version', default=None, required=False)
@click.argument('options', default=None, required=False)
def create_website(cfg: Config, ctx, name, type, version, options):
    """
    Creates a magneto 2 webshop with given name
    Arguments:
        name: The name of the website
        type: community or enterprise
        version: Set the magento version being installed. Example 2.2.8
        options: add options to the composer create project commando
    """
    args = list(filter(None, [name, type, version, options]))
    container.build_cmd(cfg.WDE_NAME, 'create_website ' + ' '.join(args)).exec_it()
    ctx.invoke(wde.cli.secure, quiet=False, domain=name)


@prelude.command()
@click.pass_context
@pass_config
@click.argument('name')
def import_website(cfg: Config, ctx, name):
    """
    Imports magento 2 webshop with given name
    Arguments:
        name: The name of the website
    """
    container.build_cmd(cfg.WDE_NAME, 'create_website ' + name, req_mount=True, cwd=cfg.DOMAIN_PATH).exec_it()
    ctx.invoke(wde.cli.secure, name)

from wde.config import Config
from wde import container, cli

from wdm.cli import *


@prelude.command()
@click.argument('args', nargs=-1, type=click.UNPROCESSED)
@pass_config
def cld(cfg: Config, args):
    """Calls composer lib development"""
    container.exec(cfg.WDE_NAME, ['composer_lib_development'] + args, require_mounted=True)


@prelude.command()
@click.pass_context
def composer_lib_development(ctx):
    """Calls composer lib development"""
    ctx.invoke(cld)


@prelude.command()
@click.argument('args', nargs=-1, type=click.UNPROCESSED)
@pass_config
def magerun2(cfg: Config, args):
    """Calls magerun 2 with given arguments"""
    container.exec(cfg.WDE_NAME, ['magerun2'] + args, require_mounted=True)


@prelude.command()
@click.pass_context
def m2(ctx):
    """Calls magerun 2 with given arguments"""
    ctx.invoke(magerun2)


@prelude.command()
@click.argument('args', nargs=-1, type=click.UNPROCESSED)
@pass_config
def magerun(cfg: Config, args):
    """Calls magerun with given arguments"""
    container.exec(cfg.WDE_NAME, ['magerun2'] + args, require_mounted=True)


@prelude.command()
@click.pass_context
def m(ctx):
    """Calls magerun with given arguments"""
    ctx.invoke(magerun)

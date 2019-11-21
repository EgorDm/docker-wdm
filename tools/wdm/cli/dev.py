from wde.config import Config
from wde import container, cli
from wdm.cli import *


@prelude.command()
@click.argument('args', nargs=-1)
@pass_config
def composer_lib_development(cfg: Config, args):
    """Calls composer lib development"""
    container.build_cmd(cfg.WDE_NAME, ['composer_lib_development'] + list(args), req_mount=True, shell=True).exec_it()


@prelude.command()
@click.argument('args', nargs=-1)
@click.pass_context
def cld(ctx, args):
    """Calls composer lib development"""
    ctx.invoke(composer_lib_development, args=args)


@prelude.command()
@click.argument('args', nargs=-1)
@pass_config
def magerun2(cfg: Config, args):
    """Calls magerun 2 with given arguments"""
    container.build_cmd(cfg.WDE_NAME, ['magerun2'] + list(args), req_mount=True, shell=True).exec_it()


@prelude.command()
@click.argument('args', nargs=-1)
@click.pass_context
def m2(ctx, args):
    """Calls magerun 2 with given arguments"""
    ctx.invoke(magerun2, args=args)


@prelude.command()
@click.argument('args', nargs=-1)
@pass_config
def magerun(cfg: Config, args):
    """Calls magerun with given arguments"""
    container.build_cmd(cfg.WDE_NAME, ['magerun'] + list(args), req_mount=True, shell=True).exec_it()


@prelude.command()
@click.argument('args', nargs=-1)
@click.pass_context
def m(ctx, args):
    """Calls magerun with given arguments"""
    ctx.invoke(magerun, args=args)

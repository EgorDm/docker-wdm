import os
import subprocess

from wdm.cli import *
from wdm import config
from wde import utils
import wde.cli
import wde.config as wconfig


@prelude.command()
@click.pass_context
def install(ctx):
    """Installs the wdm environment"""
    utils.cmd_expect(
        f'docker info',
        'Check if docker is installed, the service is running and you have permissions to run the docker command.'
    )

    click.secho('Installing WDE', color='white')
    if not os.path.exists(config.WDE_ROOT_FOLDER):
        click.echo(f'Cloning wde into {config.WDE_ROOT_FOLDER}')
        utils.cmd_expect(
            f'git clone https://github.com/EgorDm/docker-wde.git {config.WDE_ROOT_FOLDER}',
            'Failed cloning wde',
            hide_output=False
        )

    click.secho('Installing WDM', color='white')
    if not os.path.exists(config.ROOT_FOLDER):
        click.echo(f'Cloning wde into {config.ROOT_FOLDER}')
        utils.cmd_expect(
            f'git clone https://github.com/EgorDm/docker-wdm.git {config.ROOT_FOLDER}',
            'Failed cloning wdm',
            hide_output=False
        )

        utils.cmd_expect(
            ['cp', '.env.example', '.env'],
            'Failed updating .env file',
            cwd=config.ROOT_FOLDER
        )

        utils.update_ini('DOMAIN_PATH',
                         click.prompt('Enter path for your domains folder', default=os.path.expanduser('~/domains')))
        utils.update_ini('MAGENTO_MARKETPLACE_USER', click.prompt('Enter your magento marketplace user token'))
        utils.update_ini('MAGENTO_MARKETPLACE_PASS', click.prompt('Enter your magento marketplace user password'))
        utils.update_ini('MAGENTO_USERNAME', click.prompt('Enter your magento username', default='magnetron'))
        utils.update_ini('MAGENTO_PASSWORD', click.prompt('Enter your magento password', default='Magnetr0n!'))

    ctx.ensure_object(wde.config.Config)
    ctx.invoke(wde.cli.up, build=True)
    ctx.invoke(wde.cli.down)

    install_script = os.path.join(config.WDE_ROOT_FOLDER, 'scripts/install.sh')
    subprocess.run(
        f'sudo -S bash {install_script} {wconfig.get().WDE_ADDRESS}',
        shell=True,
        capture_output=False
    )
    click.secho('Sucessfully installed WDE', color='green')

import click
import platform

from configuration_repository import LocalConfigurationRepository
from daemons import HardwareObserverDaemon, ConfigurationChanged
from entities.configuration.hardware import HardwareConfiguration


def print_system_info():
    print('=' * 40, 'System Information', '=' * 40)
    uname = platform.uname()
    print(f'System: {uname.system}')
    print(f'Node Name: {uname.node}')
    print(f'Release: {uname.release}')
    print(f'Version: {uname.version}')
    print(f'Machine: {uname.machine}')
    print(f'Processor: {uname.processor}')


@click.group()
def cli():
    pass


@click.command()
def save_configuration():
    LocalConfigurationRepository.set(
        '/tmp/hardware_configuration',
        HardwareConfiguration()
    )


@click.command()
def run():
    saved_configuration = LocalConfigurationRepository.get('/tmp/hardware_configuration')
    hw_daemon = HardwareObserverDaemon(saved_configuration=saved_configuration)
    try:
        hw_daemon.run()
    except ConfigurationChanged as e:
        pass
        # send alarm and logout


cli.add_command(save_configuration)
cli.add_command(run)

if __name__ == '__main__':
    cli()

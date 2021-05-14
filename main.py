import click
import platform

from configuration.hardware import HardwareConfiguration
from configuration_repository import LocalConfigurationRepository

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
    actual_configuration = HardwareConfiguration()
    print(saved_configuration)
    print(actual_configuration)


cli.add_command(save_configuration)
cli.add_command(run)

if __name__ == '__main__':
    cli()

import click

from configuration_repository import LocalConfigurationRepository
from daemons import ObserverDaemon, ConfigurationChanged
from entities.configuration.hardware import HardwareConfiguration
from entities.configuration.software import SoftwareConfiguration


@click.group()
def cli():
    pass


@click.command()
def save_hardware_configuration():
    LocalConfigurationRepository.set(
        '/tmp/hardware_configuration',
        HardwareConfiguration()
    )


@click.command()
def save_software_configuration():
    LocalConfigurationRepository.set(
        '/tmp/software_configuration',
        SoftwareConfiguration()
    )


@click.command()
def run_hardware_daemon():
    saved_configuration = LocalConfigurationRepository.get('/tmp/hardware_configuration')
    hw_daemon = ObserverDaemon(
        saved_configuration=saved_configuration,
        configuration_getter=HardwareConfiguration,
    )
    try:
        hw_daemon.run()
    except ConfigurationChanged as e:
        pass
        # send alarm and logout


@click.command()
def run_software_daemon():
    saved_configuration = LocalConfigurationRepository.get('/tmp/software_configuration')
    sw_daemon = ObserverDaemon(
        saved_configuration=saved_configuration,
        configuration_getter=SoftwareConfiguration,
    )
    try:
        sw_daemon.run()
    except ConfigurationChanged as e:
        pass
        # send alarm and logout


@click.command()
def run():
    # TODO: run all daemons
    pass


cli.add_command(save_hardware_configuration)
cli.add_command(save_software_configuration)
cli.add_command(run_hardware_daemon)
cli.add_command(run_software_daemon)


if __name__ == '__main__':
    cli()

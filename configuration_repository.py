import json

from entities.configuration import SoftwareConfiguration
from entities.configuration.base import Configuration
from entities.configuration.hardware import HardwareConfiguration


class ConfigurationRepository:
    """Class for abstraction on place, where Configuration must be stored"""

    @classmethod
    def set(cls, key: str, conf: Configuration) -> None:
        ...

    @classmethod
    def get(cls, key: str) -> Configuration:
        ...


class LocalConfigurationRepository(ConfigurationRepository):
    """Class to store configuration in local storage"""

    @classmethod
    def set(cls, key: str, conf: Configuration) -> None:
        with open(key, 'w') as f:
            f.write(conf.json())

    @classmethod
    def get(cls, key: str) -> Configuration:
        with open(key, 'r') as f:
            data = json.loads(f.read())
            configuration_class = data.get('class_')
            if configuration_class == 'HardwareConfiguration':
                return HardwareConfiguration(**data)
            elif configuration_class == 'SoftwareConfiguration':
                return SoftwareConfiguration(**data)
            else:
                raise Exception

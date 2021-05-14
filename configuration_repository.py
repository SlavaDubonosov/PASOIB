import json

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
            return HardwareConfiguration.from_dict(
                json.loads(f.read())
            )

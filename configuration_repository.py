from configuration.base import Configuration


class ConfigurationRepository:
    """Class for abstraction on place, where Configuration must be stored"""

    def set(self, conf: Configuration) -> None:
        ...

    def get(self) -> Configuration:
        ...


class LocalConfigurationRepository(ConfigurationRepository):
    """Class to store configuration in local storage"""

    def set(self, conf: Configuration) -> None:
        ...

    def get(self) -> Configuration:
        ...


class RemoteConfigurationRepository(ConfigurationRepository):
    """Class to store configuration in remote storage"""

    def set(self, conf: Configuration) -> None:
        ...

    def get(self) -> Configuration:
        ...


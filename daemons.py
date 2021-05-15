import time
from typing import Callable

from pydantic import BaseModel

from entities.configuration.base import Configuration


class ConfigurationChanged(Exception):
    pass


class ObserverDaemon(BaseModel):
    saved_configuration: Configuration
    configuration_getter: Callable[[], Configuration]

    def run(self):
        while not self._need_to_stop:
            self._process()
            time.sleep(1)

    @property
    def _need_to_stop(self):
        return False

    def _process(self):
        actual_configuration = self.configuration_getter()
        if not actual_configuration == self.saved_configuration:
            raise ConfigurationChanged(self.configuration_getter.__name__)

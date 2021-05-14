import time

from pydantic import BaseModel

from entities.configuration.base import Configuration
from entities.configuration.hardware import HardwareConfiguration


class HardwareObserverDaemon(BaseModel):
    class HardwareConfigurationChanged(Exception):
        pass

    saved_configuration: Configuration

    def run(self):
        while not self._need_to_stop:
            self._process()
            time.sleep(1)

    @property
    def _need_to_stop(self):
        return False

    def _process(self):
        actual_configuration = HardwareConfiguration()
        if not actual_configuration == self.saved_configuration:
            raise self.HardwareConfigurationChanged()

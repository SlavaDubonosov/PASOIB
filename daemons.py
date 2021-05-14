import time


class HardwareObserverDaemon:
    def run(self):
        while not self._need_to_stop:
            self._process()
            time.sleep(1)

    @property
    def _need_to_stop(self):
        return False

    def _process(self):
        pass

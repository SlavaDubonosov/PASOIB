import subprocess

from entities.configuration.base import Configuration
from entities.software_handlers import Software


class SoftwareConfiguration(Configuration):
    software: list[Software] = None

    class_ = 'SoftwareConfiguration'

    def __init__(
        self,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.software = self._get_software()

    @staticmethod
    def _get_software() -> list[Software]:
        rpm_output = subprocess.run(
            ['yum', 'list', 'installed'],
            stdout=subprocess.PIPE
        )
        software_list = rpm_output.stdout.decode().split('\n')
        software_list = [
            sw.split()
            for sw in software_list[1:]
        ]

        return []

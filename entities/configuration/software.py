import subprocess
from typing import Iterable, Optional, Any

from entities.configuration.base import Configuration
from entities.software_handlers import Software


class SoftwareConfiguration(Configuration):
    software: list[Software] = None
    class_ = 'SoftwareConfiguration'

    def __init__(
        self,
        software: Optional[list[dict[str, Any]]] = None,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        if not software:
            self.software = list(self._get_software())
        else:
            self.software = [
                Software(**sw)
                for sw in software
            ]

    @staticmethod
    def _get_software() -> Iterable[Software]:
        rpm_output = subprocess.run(
            ['yum', 'list', 'installed'],
            stdout=subprocess.PIPE
        )
        software_raw_strs = rpm_output.stdout.decode().split('\n')
        software_raw_list = [
            sw.split()
            for sw in software_raw_strs[1:-1]
        ]
        for sw in software_raw_list:
            yield Software(
                name=sw[0],
                version=sw[1],
            )

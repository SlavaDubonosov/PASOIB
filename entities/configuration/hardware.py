import json
import subprocess
from typing import Any, Optional

from entities.configuration.base import Configuration
from entities.hardware_handlers import HardwareEntities
from entities.hardware_types import Hardware, USB


class HardwareConfiguration(Configuration):
    hardware: list[Hardware] = None
    usb: list[USB] = None
    class_: str = 'HardwareConfiguration'

    def __init__(
        self,
        hardware: Optional[list[dict[str, Any]]] = None,
        usb: Optional[list[dict[str, Any]]] = None,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        if not hardware:
            self.hardware = list(self._get_hardware())
        else:
            self.hardware = [
                HardwareEntities.get_entity(hw)
                for hw in hardware
            ]

        if not usb:
            self.usb = list(self._get_usb())
        else:
            self.usb = [USB(**u) for u in usb]

    @staticmethod
    def _get_hardware() -> list[Hardware]:
        lshw_output_in_json = subprocess.run(
            ['lshw', '-json'],
            stdout=subprocess.PIPE
        )
        hardware_info = json.loads(lshw_output_in_json.stdout)
        for child in hardware_info.get('children', []):
            for subchild in child.get('children', []):
                yield HardwareEntities.get_entity(subchild)

    @staticmethod
    def _get_usb() -> list[USB]:
        lsusb_str_list = subprocess.run(
            ['lsusb'],
            stdout=subprocess.PIPE
        ).stdout.split(b'\n')

        for lsusb_str in lsusb_str_list:
            if not lsusb_str:
                continue

            yield USB.init(lsusb_str)

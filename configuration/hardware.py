import json
import subprocess

from configuration.base import Configuration
from entities.hardware_handlers import HardwareEntities
from entities.hardware_types import Hardware, USB


class HardwareConfiguration(Configuration):
    hardware: list[Hardware] = None
    usb: list[USB] = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hardware = list(self._get_hardware())
        self.usb = list(self._get_usb())

    @staticmethod
    def _get_hardware() -> list[Hardware]:
        lshw_output_in_json = subprocess.run(
            ['lshw', '-json'],
            stdout=subprocess.PIPE
        )
        hardware_info = json.loads(lshw_output_in_json.stdout)
        for child in hardware_info.get('children', []):
            for subchild in child.get('children', []):
                yield HardwareEntities.get_entities(subchild)

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

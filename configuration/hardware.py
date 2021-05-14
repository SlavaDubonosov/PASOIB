import json
import subprocess

from configuration.base import Configuration
from entities.hardware_handlers import Hardware, HardwareEntities, USB


class HardwareConfiguration(Configuration):
    @property
    def items(self) -> list[Hardware]:
        hardware_devices = list(self._get_hardware_list())
        usb_devices = list(self._get_usb_list())

        return hardware_devices + usb_devices

    def _get_hardware_list(self) -> list[Hardware]:
        lshw_output_in_json = subprocess.run(
            ['lshw', '-json'],
            stdout=subprocess.PIPE
        )
        hardware_info = json.loads(lshw_output_in_json.stdout)
        for child in hardware_info.get('children', []):
            for subchild in child.get('children', []):

                yield HardwareEntities.get_hardware(subchild)

    def _get_usb_list(self) -> list[USB]:
        lsusb_str_list = subprocess.run(
            ['lsusb'],
            stdout=subprocess.PIPE
        ).stdout.split(b'\n')

        for lsusb_str in lsusb_str_list:
            if not lsusb_str:
                continue

            yield USB.init(lsusb_str)

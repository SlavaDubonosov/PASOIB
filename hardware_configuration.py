import json
import subprocess

from device_handlers import Device, Devices, USB


class HardwareConfiguration:
    @property
    def devices(self) -> list[Device]:
        hardware_devices = list(self._get_hardware_list())
        usb_devices = list(self._get_usb_list())

        return hardware_devices + usb_devices

    def _get_hardware_list(self) -> list[Device]:
        lshw_output_in_json = subprocess.run(
            ['lshw', '-json'],
            stdout=subprocess.PIPE
        )
        hardware_info = json.loads(lshw_output_in_json.stdout)
        for child in hardware_info.get('children', []):
            for subchild in child.get('children', []):

                yield Devices.get_device(subchild)

    def _get_usb_list(self) -> list[USB]:
        lsusb_str_list = subprocess.run(
            ['lsusb'],
            stdout=subprocess.PIPE
        ).stdout.split(b'\n')

        for lsusb_str in lsusb_str_list:
            if not lsusb_str:
                continue

            yield USB.init(lsusb_str)

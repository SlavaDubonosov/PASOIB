import json
import platform
import subprocess
from typing import Type

from device_handlers import Device, Unknown, Memory, Processor, Bridge, Generic


class SettingsRepository:
    def get(self):
        pass


class Devices:
    DEVICE_HANDLERS_MAP = {
        'memory': Memory,
        'processor': Processor,
        'bridge': Bridge,
        'generic': Generic,
    }

    @classmethod
    def get_name(cls, data):
        class_ = data['class']
        handler: Type[Device] = cls.DEVICE_HANDLERS_MAP.get(class_, Unknown)

        return handler.get_name(data)


def print_system_info():
    print('=' * 40, 'System Information', '=' * 40)
    uname = platform.uname()
    print(f'System: {uname.system}')
    print(f'Node Name: {uname.node}')
    print(f'Release: {uname.release}')
    print(f'Version: {uname.version}')
    print(f'Machine: {uname.machine}')
    print(f'Processor: {uname.processor}')


def get_hardware_list():
    lshw_output_in_json = subprocess.run(
        ['lshw', '-json'],
        stdout=subprocess.PIPE
    )
    hardware_info = json.loads(lshw_output_in_json.stdout)
    for child in hardware_info.get('children', []):
        for subchild in child.get('children', []):

            print(Devices.get_name(subchild))


def get_usb_list():
    lsusb = subprocess.run(['lsusb'], stdout=subprocess.PIPE)


def get_software_list():
    pass


if __name__ == '__main__':
    print_system_info()
    get_hardware_list()
    get_usb_list()

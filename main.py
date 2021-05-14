import platform

from configuration.hardware import HardwareConfiguration


def print_system_info():
    print('=' * 40, 'System Information', '=' * 40)
    uname = platform.uname()
    print(f'System: {uname.system}')
    print(f'Node Name: {uname.node}')
    print(f'Release: {uname.release}')
    print(f'Version: {uname.version}')
    print(f'Machine: {uname.machine}')
    print(f'Processor: {uname.processor}')


def get_software_list():
    pass


if __name__ == '__main__':
    print_system_info()
    for device in HardwareConfiguration().items:
        print(device)

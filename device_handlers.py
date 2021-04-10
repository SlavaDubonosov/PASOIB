from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Device(ABC):
    data: dict[str, str]

    @classmethod
    def init(cls, raw_data) -> 'Device':
        return cls(raw_data)

    @abstractmethod
    def get_name(self):
        ...


class Unknown(Device):
    def get_name(self):
        return self.data.get('product', 'Unknown')


class Memory(Device):
    def get_name(self):
        return self.data['description']


class Processor(Device):
    def get_name(self):
        return self.data['product']


class Bridge(Device):
    def get_name(self):
        return self.data['product']


class Generic(Device):
    def get_name(self):
        return self.data['product']


class System(Device):
    def get_name(self):
        return self.data['product']


class USB(Device):
    @classmethod
    def init(cls, raw_data) -> 'USB':
        parts = raw_data.decode().split()
        data = {
            parts[0]: parts[1],
            parts[2]: parts[3],
            parts[4]: parts[5],
            'name': ' '.join(parts[6:]),
        }
        return cls(data)

    def get_name(self):
        return self.data['name']


class Devices:
    DEVICES_MAP = {
        'memory': Memory,
        'processor': Processor,
        'bridge': Bridge,
        'generic': Generic,
        'system': System,
    }

    @classmethod
    def get_device(cls, data):
        class_ = data['class']
        device_class = cls.DEVICES_MAP.get(class_, Unknown)
        device = device_class.init(data)

        return device

    @classmethod
    def get_name(cls, data):
        device = cls.get_device(data)

        return device.get_name()

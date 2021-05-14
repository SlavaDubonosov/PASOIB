from abc import ABC
from dataclasses import dataclass


@dataclass
class Hardware(ABC):
    data: dict[str, str]

    @classmethod
    def init(cls, raw_data) -> 'Hardware':
        return cls(raw_data)

    def get_name(self) -> str:
        ...


class Unknown(Hardware):
    def get_name(self) -> str:
        return self.data.get('product', 'Unknown')


class Memory(Hardware):
    def get_name(self) -> str:
        return self.data['description']


class Processor(Hardware):
    def get_name(self) -> str:
        return self.data['product']


class Bridge(Hardware):
    def get_name(self) -> str:
        return self.data['product']


class Generic(Hardware):
    def get_name(self) -> str:
        return self.data['product']


class System(Hardware):
    def get_name(self) -> str:
        return self.data['product']


class USB(Hardware):
    @classmethod
    def init(cls, raw_data: bytes) -> 'USB':
        parts = raw_data.decode().split()
        data = {
            parts[0]: parts[1],
            parts[2]: parts[3],
            parts[4]: parts[5],
            'name': ' '.join(parts[6:]),
        }
        return cls(data)

    def get_name(self) -> str:
        return self.data['name']


class HardwareEntities:
    HARDWARES_MAP = {
        'memory': Memory,
        'processor': Processor,
        'bridge': Bridge,
        'generic': Generic,
        'system': System,
    }

    @classmethod
    def get_hardware(cls, data: dict[str, str]) -> Hardware:
        class_ = data['class']
        hardware_class = cls.HARDWARES_MAP.get(class_, Unknown)
        hardware = hardware_class.init(data)

        return hardware

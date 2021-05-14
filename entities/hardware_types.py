from pydantic import BaseModel


class Hardware(BaseModel):
    id: str
    physid: str
    vendor: str = ''
    description: str = ''
    product: str = 'unknown'
    class_: str = 'unknown'

    def get_name(self) -> str:
        return self.product


class Unknown(Hardware):
    pass


class Memory(Hardware):
    class_: str = 'memory'

    def get_name(self) -> str:
        return self.description


class Processor(Hardware):
    businfo: str
    class_: str = 'processor'


class Bridge(Hardware):
    handle: str
    class_: str = 'bridge'


class Generic(Hardware):
    handle: str
    class_: str = 'generic'


class System(Hardware):
    class_: str = 'system'


class USB(BaseModel):
    bus: str
    device: str
    id: str
    name: str
    class_: str = 'usb'

    @classmethod
    def init(cls, raw_data: bytes) -> 'USB':
        parts = raw_data.decode().lower().split()
        data = {
            parts[0]: parts[1],
            parts[2]: parts[3],
            parts[4]: parts[5],
            'name': ' '.join(parts[6:]),
        }
        return cls(**data)

    def get_name(self) -> str:
        return self.name

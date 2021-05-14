from entities.hardware_types import Hardware, Unknown, Memory, Processor, Bridge, Generic, System


class HardwareEntities:
    HARDWARES_MAP = {
        'memory': Memory,
        'processor': Processor,
        'bridge': Bridge,
        'generic': Generic,
        'system': System,
    }

    @classmethod
    def get_entities(cls, data: dict[str, str]) -> Hardware:
        class_ = data['class']
        hardware_class = cls.HARDWARES_MAP.get(class_, Unknown)
        hardware = hardware_class(**data)

        return hardware

from configuration.base import Configuration
from entities.software_handlers import Software


class SoftwareConfiguration(Configuration):
    @property
    def items(self) -> list[Software]:
        return []

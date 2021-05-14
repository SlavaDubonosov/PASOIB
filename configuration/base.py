from typing import Any


class Configuration:
    @property
    def items(self) -> list[Any]:
        return []

    def as_dict(self) -> dict[str, Any]:
        ...

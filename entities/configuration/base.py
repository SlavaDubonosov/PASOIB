from typing import Any

from pydantic import BaseModel


class Configuration(BaseModel):
    @classmethod
    def from_dict(cls, data: dict[str, Any]):
        ...

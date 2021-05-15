from pydantic import BaseModel


class Software(BaseModel):
    name: str
    version: str
    class_: str = 'software'

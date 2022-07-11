from pydantic.main import BaseModel
from datetime import datetime
from typing import Optional

from src.domain.entities.enums import ACCESS_LEVEL, ROLE


class DbBaseModel():
    id: int
    name: str
    ra: str
    year: int
    course: str
#    subject: List
    email: str

    def __init__(self, data: dict):
        self.id = data.get('id')
        self.name = data.get('name')
        self.ra = str(data.get('ra'))
        self.year = (data.get('year'))
        self.course = data.get('course')
#        self.subject = data.get('course')
        self.email = data.get('email')

    def to_dict(self):
        return self.__dict__




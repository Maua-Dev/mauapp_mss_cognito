from datetime import datetime
from typing import Optional, List
from pydantic.main import BaseModel
from pydantic import validator

from src.domain.errors.errors import EntityError


class User(BaseModel):
    id: int
    name: str
    ra: str
    year: int
    course: str
#    subject: List
    image: str

    @validator('name')
    def name_is_not_empty(cls,v: str)-> str:
        if len(v) == 0:
            raise EntityError('Name')
        return v.title()

    @validator('ra')
    def ra_is_not_invalid(cls, v: str) -> str:
        if v != None and len(str(v)) != 8:
            raise EntityError('ra')
        return str(v)

    @validator('year')
    def year_is_not_invalid(cls, v: int) -> int:
        if v != None:
            raise EntityError('year')
        return int(v)

    @validator('course')
    def course_is_not_empty(cls, v: str) -> str:
        if len(v) == 0:
            raise EntityError('course')
        return str(v)

    @validator('image')
    def image_is_not_empty(cls, v: str) -> str:
        if len(v) == 0:
            raise EntityError('image')
        return str(v)
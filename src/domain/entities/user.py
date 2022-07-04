from datetime import datetime
from typing import Optional, List
from pydantic.main import BaseModel
from pydantic import validator

from src.domain.entities.enums import YEAR_ENUM, DegreeEnum
from src.domain.errors.errors import EntityError


class User(BaseModel):
    id: Optional[str]
    name: str
    ra: str
    year: YEAR_ENUM
    course: DegreeEnum
    email: str
    password: Optional[str]


    @validator('id')
    def id_validator(cls, v):
        return v


    @validator('name')
    def name_is_not_empty(cls,v: str)-> str:
        if len(v) == 0:
            raise EntityError('Name')
        return v.title()

    @validator('ra')
    def ra_is_not_invalid(cls, v: str) -> str:
        if v == None or len(str(v)) != 8:
            raise EntityError('ra')
        return str(v)

    @validator('year')
    def year_is_not_invalid(cls, v: int) -> int:
        if v is None:
            raise EntityError('year')
        return v

    @validator('course')
    def course_is_not_empty(cls, v: str) -> str:
        if v is None:
            raise EntityError('course')
        return v

    @validator('password')
    def password_is_not_empty(cls, v:str) -> str:
        if v is None:
            return v
        if len(v) < 8:
            raise EntityError('Password too short')
        return v


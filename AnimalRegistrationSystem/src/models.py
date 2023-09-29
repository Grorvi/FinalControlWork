from datetime import date
from typing import TypeVar, List, Optional

from pydantic import BaseModel, constr, Field

T = TypeVar('T')


class Animal(BaseModel):
    id: str | None = None
    name: str = Field(max_length=20)
    birthday: date
    commands: str | None = Field(max_length=50)
    genus_name: str = Field(max_length=20)


class Response(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T] = None
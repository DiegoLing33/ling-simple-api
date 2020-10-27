#  ██╗░░░░░██╗███╗░░██╗░██████╗░░░░██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
#  ██║░░░░░██║████╗░██║██╔════╝░░░░██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
#  ██║░░░░░██║██╔██╗██║██║░░██╗░░░░██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
#  ██║░░░░░██║██║╚████║██║░░╚██╗░░░██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
#  ███████╗██║██║░╚███║╚██████╔╝░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
#  ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
#
#  Developed by Yakov V. Panov (C) Ling • Black 2020
#  @site http://ling.black
from typing import Optional, List

from pydantic.main import BaseModel

from database.core.schemas import CoreSchema


class NoteBase(BaseModel):
    title: str
    content: str
    url: Optional[str]


class NoteCreate(NoteBase):
    pass


class NoteMeta(object):
    pass


class Note(NoteBase, CoreSchema):
    id: int

    meta: List[NoteMeta]

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class NoteMetaBase(BaseModel):
    """
    The base schema class
    """
    note_id: int
    field: str
    value: str


class NoteMetaCreate(NoteMetaBase):
    pass


class NoteMeta(NoteMetaBase, CoreSchema):
    id: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

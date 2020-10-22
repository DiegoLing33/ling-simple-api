#  ██╗░░░░░██╗███╗░░██╗░██████╗░░░░██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
#  ██║░░░░░██║████╗░██║██╔════╝░░░░██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
#  ██║░░░░░██║██╔██╗██║██║░░██╗░░░░██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
#  ██║░░░░░██║██║╚████║██║░░╚██╗░░░██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
#  ███████╗██║██║░╚███║╚██████╔╝░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
#  ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
#
#  Developed by Yakov V. Panov (C) Ling • Black 2020
#  @site http://ling.black
from typing import List

from pydantic.main import BaseModel

from core.response import RequestLimit
from database.schemas import UserGroup, UserMeta, User


class ResponseGroupsList(BaseModel):
    items: List[UserGroup]
    count: int


class ResponseUserMetaList(BaseModel):
    items: List[UserMeta]
    count: int


class ResponseUsersList(BaseModel):
    items: List[User]
    count: int


class ResponseGroups(BaseModel):
    response: ResponseGroupsList
    request: RequestLimit


class ResponseUsers(BaseModel):
    response: ResponseUsersList
    request: RequestLimit


class ResponseUserMeta(BaseModel):
    response: ResponseUserMetaList
    request: RequestLimit

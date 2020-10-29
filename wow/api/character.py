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

from pydantic import BaseModel
from sqlalchemy.orm import Session

from core.response import RequestLimit
from database import DatabaseUtils
from wow.database.models import CharacterModel
from wow.interface.entity import Character


class CharacterAPIList(BaseModel):
    items: List[Character]
    count: int


class CharacterAPIListResponse(BaseModel):
    response: CharacterAPIList
    request: RequestLimit


class CharacterAPI:

    @staticmethod
    def list(db: Session, limit: int = 100, offset: int = 0):
        return DatabaseUtils.limited_results(db, CharacterModel, limit=limit, offset=offset)

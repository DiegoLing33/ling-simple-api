#  ██╗░░░░░██╗███╗░░██╗░██████╗░░░░██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
#  ██║░░░░░██║████╗░██║██╔════╝░░░░██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
#  ██║░░░░░██║██╔██╗██║██║░░██╗░░░░██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
#  ██║░░░░░██║██║╚████║██║░░╚██╗░░░██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
#  ███████╗██║██║░╚███║╚██████╔╝░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
#  ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
#
#  Developed by Yakov V. Panov (C) Ling • Black 2020
#  @site http://ling.black
from fastapi import APIRouter, Depends

from database import get_db
from wow.api import CharacterAPI
from wow.api.character import CharacterAPIListResponse
from wow.database.models import CharacterModel
from wow.interface.entity import Character

router = APIRouter()


@router.get(
    "/list",
    response_model=CharacterAPIListResponse,
    summary="Returns all characters in the guild with equipment and extra data"
)
def get_characters_list(offset: int = 0, limit: int = 100, db=Depends(get_db)):
    return CharacterAPI.list(db, limit, offset)


@router.get(
    "/{name}",
    response_model=Character,
    summary="Returns the requested by name character with equipment and extra data"
)
def get_character(name: str, db=Depends(get_db)):
    name = name.title()
    return db.query(CharacterModel).filter(CharacterModel.name == name).first()

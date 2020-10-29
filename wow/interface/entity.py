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

from pydantic import BaseModel

CharacterEquipmentTypesList = [
    "HEAD", "NECK", "SHOULDER", "CHEST",

    # Пояс
    "WAIST",
    "LEGS",

    # Ступни
    "FEET",

    # Запястья
    "WRIST",

    # Кисти рук
    "HANDS",

    "FINGER_1",
    "FINGER_2",
    "TRINKET_1",
    "TRINKET_2",

    "BACK"
    "MAIN_HAND",
    "OFF_HAND",

    # Накидка
    "TABARD",
]


class CharacterEquipment(BaseModel):
    """
    Entity of the equipment item

    For e.g. hand
    """
    wow_id: int
    character_id: int
    image_id: Optional[int]

    title: str

    slot: str
    inventory_type: str
    level: int

    quantity: int
    quality: str

    item_class_id: int
    item_subclass_id: int

    stats: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class CharacterRace(BaseModel):
    wow_id: int
    title: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class CharacterClass(BaseModel):
    wow_id: int
    title: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class CharacterActiveSpec(BaseModel):
    wow_id: int
    title: str
    type: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class Character(BaseModel):
    wow_id: int

    name: str
    gender: str
    level: int

    faction: str

    character_race_id: int
    character_race: Optional[CharacterRace]

    character_class_id: int
    character_class: Optional[CharacterClass]

    character_spec_id: int
    character_spec: Optional[CharacterActiveSpec]

    realm_id: int
    guild_id: int

    equipment: Optional[List[CharacterEquipment]]

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

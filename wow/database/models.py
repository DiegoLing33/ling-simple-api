#  ██╗░░░░░██╗███╗░░██╗░██████╗░░░░██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
#  ██║░░░░░██║████╗░██║██╔════╝░░░░██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
#  ██║░░░░░██║██╔██╗██║██║░░██╗░░░░██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
#  ██║░░░░░██║██║╚████║██║░░╚██╗░░░██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
#  ███████╗██║██║░╚███║╚██████╔╝░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
#  ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
#
#  Developed by Yakov V. Panov (C) Ling • Black 2020
#  @site http://ling.black
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from database import Base
from database.core.models import CoreModel


class CharacterRaceModel(Base, CoreModel):
    __tablename__ = "characters_races"
    wow_id = Column(Integer)
    title = Column(String)


class CharacterRoleModel(Base, CoreModel):
    __tablename__ = "characters_roles"
    role_index = Column(Integer)
    title = Column(String)


class CharacterClassModel(Base, CoreModel):
    __tablename__ = "characters_classes"
    wow_id = Column(Integer)
    title = Column(String)


class CharacterSpecModel(Base, CoreModel):
    __tablename__ = "characters_specs"
    wow_id = Column(Integer)
    type = Column(Integer)
    title = Column(String)


class CharacterEquipmentModel(Base, CoreModel):
    __tablename__ = "characters_equipment"

    wow_id = Column(Integer)
    character_id = Column(Integer, ForeignKey("characters.wow_id"))

    title = Column(String)
    image_id = Column(Integer)

    slot = Column(String)
    inventory_type = Column(String)
    level = Column(Integer)

    quantity = Column(Integer)
    quality = Column(String)

    item_class_id = Column(Integer)
    item_subclass_id = Column(Integer)

    stats = Column(String)

    character = relationship("CharacterModel", back_populates="equipment")


class CharacterModel(Base, CoreModel):
    """
    User meta model
    """
    __tablename__ = "characters"

    wow_id = Column(Integer)

    name = Column(String)
    level = Column(Integer)
    gender = Column(String)
    faction = Column(String)

    role_index = Column(Integer, ForeignKey("characters_roles.role_index"))
    role = relationship("CharacterRoleModel")

    character_race_id = Column(Integer, ForeignKey("characters_races.wow_id"))
    character_race = relationship("CharacterRaceModel")

    character_class_id = Column(Integer, ForeignKey("characters_classes.wow_id"))
    character_class = relationship("CharacterClassModel")

    character_spec_id = Column(Integer, ForeignKey("characters_specs.wow_id"))
    character_spec = relationship("CharacterSpecModel")

    realm_id = Column(Integer)
    guild_id = Column(Integer)

    equipment = relationship("CharacterEquipmentModel", back_populates="character")

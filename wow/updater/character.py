#  ██╗░░░░░██╗███╗░░██╗░██████╗░░░░██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
#  ██║░░░░░██║████╗░██║██╔════╝░░░░██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
#  ██║░░░░░██║██╔██╗██║██║░░██╗░░░░██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
#  ██║░░░░░██║██║╚████║██║░░╚██╗░░░██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
#  ███████╗██║██║░╚███║╚██████╔╝░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
#  ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
#
#  Developed by Yakov V. Panov (C) Ling • Black 2020
#  @site http://ling.black
import sys
import time

from progress.bar import Bar
from logzero import logger

from wow.blizzard import blizzard_guild_roster
from wow.blizzard.core import blizzard_db
from wow.database.models import CharacterModel, CharacterEquipmentModel
from wow.interface.blizzard_api import BlizzardAPI


class CharacterUpdater:

    @staticmethod
    def update_character_info(name: str, role=0):
        data = BlizzardAPI.character(name)
        db = blizzard_db()
        db.query(CharacterModel).filter(CharacterModel.wow_id == data.wow_id).delete()

        db.add(CharacterModel(
            wow_id=data.wow_id,

            name=data.name,
            level=data.level,
            gender=data.gender,
            faction=data.faction,

            role_index=role,

            character_race_id=data.character_race_id,
            character_class_id=data.character_class_id,
            character_spec_id=data.character_spec_id,

            realm_id=data.realm_id,
            guild_id=data.guild_id,
        ))
        db.commit()

    @staticmethod
    def update_equipment(name: str):
        data = BlizzardAPI.character_equipment(name)
        db = blizzard_db()

        print("")
        logger.info("Starting update character equipment " + name)
        logger.info(f"Total count: {len(data)}")
        bar = Bar('Equipment ' + name, max=len(data), fill='█')

        db.query(CharacterEquipmentModel) \
            .filter(CharacterEquipmentModel.character_id == data[0].character_id).delete()

        for item in data:
            db.add(CharacterEquipmentModel(
                title=item.title,
                wow_id=item.wow_id,
                character_id=item.character_id,

                slot=item.slot,
                inventory_type=item.inventory_type,
                level=item.level,

                quantity=item.quantity,
                quality=item.quality,

                item_class_id=item.item_class_id,
                item_subclass_id=item.item_subclass_id,
                stats=item.stats,
            ))
            bar.next()
            time.sleep(1 / 1000)
        db.commit()

    @staticmethod
    def update_character(name: str, role=0):
        CharacterUpdater.update_character_info(name, role)
        CharacterUpdater.update_equipment(name)

    @staticmethod
    def update_characters():
        data = blizzard_guild_roster()
        logger.info("Starting update characters...")
        logger.info(f"Total count: {len(data['members'])}")
        bar = Bar('Characters updating', max=len(data['members']), fill='█')
        for member in data['members']:
            name = member["character"]["name"]
            role = member["rank"]
            CharacterUpdater.update_character(name, role)
            bar.next()
        print("")

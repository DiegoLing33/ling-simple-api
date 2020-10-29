#  ██╗░░░░░██╗███╗░░██╗░██████╗░░░░██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
#  ██║░░░░░██║████╗░██║██╔════╝░░░░██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
#  ██║░░░░░██║██╔██╗██║██║░░██╗░░░░██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
#  ██║░░░░░██║██║╚████║██║░░╚██╗░░░██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
#  ███████╗██║██║░╚███║╚██████╔╝░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
#  ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
#
#  Developed by Yakov V. Panov (C) Ling • Black 2020
#  @site http://ling.black
import json
from typing import List

from wow.blizzard import blizzard_guild_info, blizzard_character, blizzard_data_classes, blizzard_data_races, \
    blizzard_data_specs, blizzard_character_equipment
from wow.interface.entity import Character, CharacterClass, CharacterRace, CharacterActiveSpec, CharacterEquipment
from wow.utils.character import get_role_by_spec_id


class BlizzardAPI:

    @staticmethod
    def guild():
        resp = blizzard_guild_info()
        return resp

    @staticmethod
    def character(name: str) -> Character:
        """
        Returns the character
        :param name:
        :return:
        """
        resp = blizzard_character(name)
        obj = Character(
            wow_id=resp['id'],
            name=resp['name'],
            level=resp['level'],
            gender=resp['gender']['type'],
            faction=resp['faction']['type'],
            character_race_id=resp['race']['id'],
            character_class_id=resp['character_class']['id'],
            character_spec_id=resp['active_spec']['id'],
            realm_id=resp['realm']['id'],
            guild_id=resp['guild']['id'],
        )
        return obj

    @staticmethod
    def classes() -> List[CharacterClass]:
        """
        Returns the classes list
        :return:
        """
        resp = blizzard_data_classes()
        arr = []
        for item in resp['classes']:
            obj = CharacterClass(
                wow_id=item['id'],
                title=item['name'],
            )
            arr.append(obj)
        return arr

    @staticmethod
    def races() -> List[CharacterRace]:
        """
        Returns the races list
        :return:
        """
        resp = blizzard_data_races()
        arr = []
        for item in resp['races']:
            obj = CharacterRace(
                wow_id=item['id'],
                title=item['name'],
            )
            arr.append(obj)
        return arr

    @staticmethod
    def specs() -> List[CharacterActiveSpec]:
        """
        Returns the specs list
        :return:
        """
        resp = blizzard_data_specs()
        arr = []
        for item in resp['character_specializations']:
            obj = CharacterActiveSpec(
                wow_id=item['id'],
                title=item['name'],
                type=get_role_by_spec_id(item['id'])
            )
            arr.append(obj)
        return arr

    @staticmethod
    def character_equipment(name: str):
        # Raw data
        resp = blizzard_character_equipment(name)
        arr = []

        # Handling
        for item in resp["equipped_items"]:
            obj = CharacterEquipment(
                wow_id=item['item']['id'],
                character_id=resp['character']['id'],

                title=item['name'],

                slot=item['slot']['type'],
                inventory_type=item['inventory_type']['type'],
                level=item['level']['value'],

                quantity=item['quantity'],
                quality=item['quality']['type'],

                item_class_id=item['item_class']['id'],
                item_subclass_id=item['item_subclass']['id'],

                stats=""
                # stats=json.dumps(item['stats'], ensure_ascii=False),
            )
            arr.append(obj)
        return arr

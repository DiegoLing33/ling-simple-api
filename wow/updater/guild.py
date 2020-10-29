#  ██╗░░░░░██╗███╗░░██╗░██████╗░░░░██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
#  ██║░░░░░██║████╗░██║██╔════╝░░░░██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
#  ██║░░░░░██║██╔██╗██║██║░░██╗░░░░██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
#  ██║░░░░░██║██║╚████║██║░░╚██╗░░░██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
#  ███████╗██║██║░╚███║╚██████╔╝░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
#  ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
#
#  Developed by Yakov V. Panov (C) Ling • Black 2020
#  @site http://ling.black
from logzero import logger

from database.client import DataStore
from wow.blizzard import blizzard_guild_info, blizzard_guild_roster
from wow.blizzard.core import blizzard_db
from wow.database.models import CharacterRaceModel, CharacterClassModel, CharacterSpecModel, CharacterEquipmentModel, \
    CharacterModel
from wow.interface.blizzard_api import BlizzardAPI


class GuildUpdater:
    @staticmethod
    def update_info():
        """
        Updates the main guild info
        :return:
        """
        db = blizzard_db()
        data = blizzard_guild_info()
        print(data)

        print(f"Guild identifier: {data['id']}")
        DataStore.set(db, "gid", data["id"])

        print(f"Guild name: {data['name']}")
        DataStore.set(db, "guild_name", data["name"])

        print(f"Guild achievement points: {data['achievement_points']}")
        DataStore.set(db, "achievement_points", data["achievement_points"])

        print(f"Guild faction: {data['faction']['name']}")
        DataStore.set(db, "faction_name", data['faction']['name'])
        DataStore.set(db, "faction_type", data['faction']['type'])

        print(f"Guild created timestamp: {data['created_timestamp']}")
        DataStore.set(db, "created_timestamp", data['created_timestamp'])

        print(f"Guild players: {data['member_count']}")
        DataStore.set(db, "players", data['member_count'])

        print(f"Guild crest: {data['crest']['emblem']['id']}")
        crest_url = f'https://render-eu.worldofwarcraft.com/guild/tabards/emblem_{data["crest"]["emblem"]["id"]}.png'
        background_color = data["crest"]["background"]["color"]["rgba"]
        background_color = f"{background_color['r']}, {background_color['g']}, {background_color['b']}, {background_color['a']}"
        DataStore.set(db, "crest_emblem_url", crest_url)
        DataStore.set(db, "crest_background_color", background_color)
        print("Done.")

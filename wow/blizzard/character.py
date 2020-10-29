#  ██╗░░░░░██╗███╗░░██╗░██████╗░░░░██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
#  ██║░░░░░██║████╗░██║██╔════╝░░░░██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
#  ██║░░░░░██║██╔██╗██║██║░░██╗░░░░██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
#  ██║░░░░░██║██║╚████║██║░░╚██╗░░░██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
#  ███████╗██║██║░╚███║╚██████╔╝░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
#  ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
#
#  Developed by Yakov V. Panov (C) Ling • Black 2020
#  @site http://ling.black
from urllib.parse import quote

from wow.blizzard.core import default_params, blizzard_request
from wow.config import guild_name, server_slug, mythic_season


def blizzard_character(
        name: str,
        server: str = server_slug,
        data=default_params,
        sleep: int = 10
):
    """
    Returns the blizzard character information
    :param name:
    :param server:
    :param data:
    :param sleep:
    :return:
    """
    name = quote(name.lower())
    return blizzard_request(
        f"profile/wow/character/{server}/{name}",
        data,
        sleep
    )


def blizzard_character_equipment(
        name: str,
        server: str = server_slug,
        data=default_params,
        sleep: int = 10
):
    """
    Returns the character equipment information
    :param name:
    :param server:
    :param data:
    :param sleep:
    :return:
    """
    name = quote(name.lower())
    return blizzard_request(
        f"profile/wow/character/{server}/{name}/equipment",
        data,
        sleep
    )


def blizzard_character_media(
        name: str,
        server: str = server_slug,
        data=default_params,
        sleep: int = 10
):
    """
    Returns the character media data
    :param name:
    :param server:
    :param data:
    :param sleep:
    :return:
    """
    name = quote(name.lower())
    return blizzard_request(
        f"profile/wow/character/{server}/{name}/character-media",
        data,
        sleep
    )


def blizzard_character_mythic_season(
        name: str,
        server: str = server_slug,
        season: int = mythic_season,
        data=default_params,
        sleep: int = 10
):
    """
    Returns character mythic season data
    :param name:
    :param server:
    :param season:
    :param data:
    :param sleep:
    :return:
    """
    return blizzard_request(
        f"profile/wow/character/{server}/{name}/mythic-keystone-profile/season/{season}",
        data,
        sleep
    )

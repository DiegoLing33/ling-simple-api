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

from wow.blizzard.core import blizzard_request, default_params
from wow.config import guild_name, server_slug


def blizzard_guild_roster(guild: str = guild_name, data=default_params, sleep: int = 10):
    """
    Returns the guild roster
    :param guild:
    :param data:
    :param sleep:
    :return:
    """
    name = quote(guild.lower())
    return blizzard_request(f"data/wow/guild/{server_slug}/{name}/roster", data, sleep)


def blizzard_guild_info(guild: str = guild_name, data=default_params, sleep: int = 10):
    """
    Returns the guild info
    :param guild:
    :param data:
    :param sleep:
    :return:
    """
    name = quote(guild.lower())
    return blizzard_request(f"data/wow/guild/{server_slug}/{name}", data, sleep)

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
from wow.config import default_static_namespace


def blizzard_data_class(
        name: str,
        data=default_params,
        sleep: int = 10,
):
    """
    Returns the game class info
    :param name:
    :param data:
    :param sleep:
    :return:
    """
    r_name = quote(name.lower())
    return blizzard_request(
        f"data/wow/playable-class/{r_name}",
        data,
        sleep,
    )


def blizzard_data_race(
        name: str,
        data=default_params,
        sleep: int = 10,
):
    """
    Returns the game race info
    :param name:
    :param data:
    :param sleep:
    :return:
    """
    r_name = quote(name.lower())
    return blizzard_request(
        f"data/wow/playable-race/{r_name}",
        data,
        sleep,
    )


def blizzard_data_classes(
        sleep=10,
        static_namespace=default_static_namespace
):
    """
    Returns the classes
    :param sleep:
    :param static_namespace:
    :return:
    """
    data = default_params
    data["namespace"] = static_namespace
    return blizzard_request(
        "data/wow/playable-class/index",
        data,
        sleep
    )


def blizzard_data_races(
        sleep=10,
        static_namespace=default_static_namespace
):
    """
    Returns the races
    :param sleep:
    :param static_namespace:
    :return:
    """
    data = default_params
    data["namespace"] = static_namespace
    return blizzard_request(
        "data/wow/playable-race/index",
        data,
        sleep
    )


def blizzard_data_specs(
        sleep=10,
        static_namespace=default_static_namespace
):
    """
    Returns the specs
    :param sleep:
    :param static_namespace:
    :return:
    """
    data = default_params
    data["namespace"] = static_namespace
    return blizzard_request(
        "data/wow/playable-specialization/index",
        data,
        sleep
    )

#  ██╗░░░░░██╗███╗░░██╗░██████╗░░░░██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
#  ██║░░░░░██║████╗░██║██╔════╝░░░░██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
#  ██║░░░░░██║██╔██╗██║██║░░██╗░░░░██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
#  ██║░░░░░██║██║╚████║██║░░╚██╗░░░██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
#  ███████╗██║██║░╚███║╚██████╔╝░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
#  ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
#
#  Developed by Yakov V. Panov (C) Ling • Black 2020
#  @site http://ling.black


import time

import requests

from database import get_db
from database.client import DataStore
from wow.config import client_id, client_secret, blizzard_api_url, default_namespace


def blizzard_db():
    return next(get_db())


default_params = dict(
    locale="ru_RU",
    namespace=default_namespace,
    access_token=None,
)


def blizzard_get_token():
    """
    Returns the blizzard token
    :return:
    """
    r = requests.post(
        "https://us.battle.net/oauth/token",
        auth=(client_id, client_secret),
        data={"grant_type": "client_credentials"}
    )
    return r.json()


def blizzard_get_token_and_save():
    """
    Gets token and saves
    :return:
    """
    token = blizzard_get_token()
    db = blizzard_db()
    DataStore.set(db, "token", value=token['access_token'])
    DataStore.set(db, "token_created", value=str(time.time()).split('.')[0])


def blizzard_support_is_token_expired():
    """
    Returns true, if token expired
    :return:
    """
    try:
        created = int(DataStore.get(blizzard_db(), "token_created").value)
    except Exception:
        created = 0
    return (time.time() - created) > 60 * 60


def blizzard_support_get_token():
    """
    Returns the token
    :return:
    """
    if blizzard_support_is_token_expired():
        blizzard_get_token_and_save()
    return DataStore.get(blizzard_db(), "token").value


def blizzard_request(path: str, data=default_params, sleep=10):
    """
    Sends the default blizzard request
    :param path:
    :param data:
    :param sleep:
    :return:
    """
    data['access_token'] = blizzard_support_get_token()
    data['locale'] = "ru_RU"
    if data['namespace'] is None:
        data['namespace'] = "profile-eu"
    api_path = blizzard_api_url + "/" + path
    r = requests.get(
        api_path,
        params=data
    )
    time.sleep(sleep / 1000)
    return r.json()


def blizzard_media(path: str):
    """
    Returns the media element
    :param path:
    :return:
    """
    data = default_params
    data['access_token'] = blizzard_support_get_token()
    data['locale'] = "ru_RU"
    if data['namespace'] is None:
        data['namespace'] = "profile-eu"
    api_path = f'https://eu.api.blizzard.com/data/wow/media/{path}?namespace=static-9.0.1_36072-eu'
    r = requests.get(
        api_path,
        params=data
    )
    time.sleep(10 / 1000)
    return r.json()

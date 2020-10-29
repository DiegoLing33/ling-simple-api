#  ██╗░░░░░██╗███╗░░██╗░██████╗░░░░██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
#  ██║░░░░░██║████╗░██║██╔════╝░░░░██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
#  ██║░░░░░██║██╔██╗██║██║░░██╗░░░░██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
#  ██║░░░░░██║██║╚████║██║░░╚██╗░░░██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
#  ███████╗██║██║░╚███║╚██████╔╝░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
#  ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
#
#  Developed by Yakov V. Panov (C) Ling • Black 2020
#  @site http://ling.black
from wow.blizzard.core import blizzard_db
from wow.config import default_items_images_path, default_characters_images_path
from wow.database.models import CharacterEquipmentModel, CharacterModel
from wow.downloaders import MediaDownloader


def connector(wow_id, image_id):
    db = blizzard_db()
    db.query(CharacterEquipmentModel).filter(CharacterEquipmentModel.wow_id == wow_id).update({'image_id': image_id})
    db.commit()


class MediaUpdater:
    """
    Updates all the media data
    """

    @staticmethod
    def update_items_images(path=default_items_images_path):
        """
        Downloads the items images

        Items are getting from the database

        :param path:  - saving path
        :return:
        """
        MediaDownloader.download_items_images(
            blizzard_db().query(CharacterEquipmentModel).all(),
            path,
            connector=connector
        )

    @staticmethod
    def update_characters_images(path=default_characters_images_path):
        """
        Downloads the characters images

        Characters are getting from the database
        :param path:
        :return:
        """
        MediaDownloader.download_characters_images(
            blizzard_db().query(CharacterModel).all(),
            path
        )

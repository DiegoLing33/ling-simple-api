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
from progress.bar import Bar

from wow.blizzard.core import blizzard_db
from wow.database.models import CharacterRaceModel, CharacterClassModel, CharacterSpecModel
from wow.interface.blizzard_api import BlizzardAPI


class StaticUpdater:
    """

    Updates static information

    Game classes, races, specializations

    """

    @staticmethod
    def update_races():
        """
        Downloads the races data
        :return:
        """
        races = BlizzardAPI.races()
        db = blizzard_db()

        logger.info("Starting downloading races...")
        logger.info(f"Total count: {len(races)}")
        bar = Bar('Races downloading', max=len(races), fill='█')

        db.query(CharacterRaceModel).delete()
        for race in races:
            db.add(CharacterRaceModel(
                title=race.title,
                wow_id=race.wow_id
            ))
            bar.next()
        db.commit()

    @staticmethod
    def update_classes():
        classes = BlizzardAPI.classes()
        db = blizzard_db()

        logger.info("Starting downloading classes...")
        logger.info(f"Total count: {len(classes)}")
        bar = Bar('Classes downloading', max=len(classes), fill='█')

        db.query(CharacterClassModel).delete()
        for item in classes:
            db.add(CharacterClassModel(
                title=item.title,
                wow_id=item.wow_id
            ))
            bar.next()
        db.commit()

    @staticmethod
    def update_specs():
        classes = BlizzardAPI.specs()
        db = blizzard_db()

        logger.info("Starting downloading specializations...")
        logger.info(f"Total count: {len(classes)}")
        bar = Bar('Specializations downloading', max=len(classes), fill='█')

        db.query(CharacterSpecModel).delete()
        for item in classes:
            print(f'Added specialization: {item.title}')
            db.add(CharacterSpecModel(
                title=item.title,
                wow_id=item.wow_id,
                type=item.type
            ))
            bar.next()
        db.commit()

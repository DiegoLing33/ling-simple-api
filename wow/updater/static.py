#  ██╗░░░░░██╗███╗░░██╗░██████╗░░░░██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
#  ██║░░░░░██║████╗░██║██╔════╝░░░░██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
#  ██║░░░░░██║██╔██╗██║██║░░██╗░░░░██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
#  ██║░░░░░██║██║╚████║██║░░╚██╗░░░██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
#  ███████╗██║██║░╚███║╚██████╔╝░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
#  ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
#
#  Developed by Yakov V. Panov (C) Ling • Black 2020
#  @site http://ling.black

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
        print('Races updating...')
        races = BlizzardAPI.races()
        db = blizzard_db()
        print(f'Got {len(races)} races...')
        print('Clearing table...')
        db.query(CharacterRaceModel).delete()
        for race in races:
            print(f'Added race: {race.title}')
            db.add(CharacterRaceModel(
                title=race.title,
                wow_id=race.wow_id
            ))
        print('Commit...')
        db.commit()
        print('Done.')

    @staticmethod
    def update_classes():
        print('Classes updating...')
        classes = BlizzardAPI.classes()
        db = blizzard_db()
        print(f'Got {len(classes)} classes...')
        print('Clearing table...')
        db.query(CharacterClassModel).delete()
        for item in classes:
            print(f'Added class: {item.title}')
            db.add(CharacterClassModel(
                title=item.title,
                wow_id=item.wow_id
            ))
        print('Commit...')
        db.commit()
        print('Done.')

    @staticmethod
    def update_specs():
        print('Specializations updating...')
        classes = BlizzardAPI.specs()
        db = blizzard_db()
        print(f'Got {len(classes)} specializations...')
        print('Clearing table...')
        db.query(CharacterSpecModel).delete()
        for item in classes:
            print(f'Added specialization: {item.title}')
            db.add(CharacterSpecModel(
                title=item.title,
                wow_id=item.wow_id,
                type=item.type
            ))
        print('Commit...')
        db.commit()
        print('Done.')

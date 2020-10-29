#  ██╗░░░░░██╗███╗░░██╗░██████╗░░░░██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
#  ██║░░░░░██║████╗░██║██╔════╝░░░░██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
#  ██║░░░░░██║██╔██╗██║██║░░██╗░░░░██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
#  ██║░░░░░██║██║╚████║██║░░╚██╗░░░██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
#  ███████╗██║██║░╚███║╚██████╔╝░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
#  ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
#
#  Developed by Yakov V. Panov (C) Ling • Black 2020
#  @site http://ling.black
import logging
import time
from datetime import datetime

import logzero

from wow.updater import GuildUpdater, CharacterUpdater, MediaUpdater


def run_cron_operation():
    """
    Operation what needs to do every hour min
    :return:
    """

    logzero.logfile(f"logs/{datetime.now().strftime('%d.%m.%Y-%H:%M:%S')}-rotating.log", maxBytes=1e6, backupCount=3)

    # Update info first
    GuildUpdater.update_info()
    time.sleep(1)

    # Then update players
    CharacterUpdater.update_characters()
    time.sleep(1)

    # And for the end update images
    MediaUpdater.update_characters_images()
    time.sleep(1)
    MediaUpdater.update_items_images()
    time.sleep(1)


if __name__ == "__main__":
    run_cron_operation()

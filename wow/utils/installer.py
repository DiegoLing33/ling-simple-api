#  ██╗░░░░░██╗███╗░░██╗░██████╗░░░░██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
#  ██║░░░░░██║████╗░██║██╔════╝░░░░██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
#  ██║░░░░░██║██╔██╗██║██║░░██╗░░░░██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
#  ██║░░░░░██║██║╚████║██║░░╚██╗░░░██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
#  ███████╗██║██║░╚███║╚██████╔╝░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
#  ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
#
#  Developed by Yakov V. Panov (C) Ling • Black 2020
#  @site http://ling.black

import os
from logzero import logger

from wow.config import default_static_path, default_items_images_path, default_characters_images_path


def wow_install():
    """
    Installation
    :return:
    """
    logger.info('Testing directories...')
    if not os.path.isdir(default_static_path):
        logger.info('Creating static path')
        os.mkdir(default_static_path)
    if not os.path.isdir(default_items_images_path):
        logger.info(f'Creating {default_items_images_path} path')
        os.mkdir(default_items_images_path)
    if not os.path.isdir(default_characters_images_path):
        logger.info(f'Creating {default_characters_images_path} path')
        os.mkdir(default_characters_images_path)
    logger.info('All directories exists!')

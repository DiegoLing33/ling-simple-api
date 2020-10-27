from typing import List

from pyfiglet import Figlet
from console_progressbar import ProgressBar

import os
import sys
from pathlib import Path

f = Figlet(font='slant')

current_path = Path(__file__).parent.parent.absolute()

#
# templates
#

SCHEMA_TEMPLATE = """from pydantic import BaseModel


class %oneBase(BaseModel):
    pass
    

class %oneCreate(%oneBase):
    pass


class %one(%oneBase):
    id: int
"""

MODEL_TEMPLATE = """from sqlalchemy import Integer, Column

from database import Base


class %oneModel(Base):
    __tablename__ = "%title"
    
    id = Column(Integer, primary_key=True, index=True)
"""

ACTIONS_TEMPLATE = """from sqlalchemy.orm import Session

from .model import %oneModel
from .schema import %oneCreate
from .. import DatabaseUtils


class %titleActions:
    #
    # The actions
    #
    @staticmethod
    def add(db: Session, item: %oneCreate):
        #
        # Adds the item
        #
        return DatabaseUtils.insert(
            db,
            db_item=%oneModel(

            )
        )

    @staticmethod
    def get_by_id(db: Session, id: int) -> %oneModel:
        #
        # Returns item by id
        #
        return db.query(%oneModel).filter(%oneModel.id == id).first()
"""

INIT_TEMPLATE = """from .actions import %titleActions
from .model import %oneModel
from .schema import %one, %oneBase, %oneCreate
"""


def header():
    """
    The header
    :return:
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f.renderText("LSA"))
    print("- - - Ling Simple API CLI - - -")
    print("")
    return input("Input command: ")


def command_create(args: List):
    """
    Runs create command
    :param args:
    :return:
    """
    if args[1] == "table":
        name = args[2]
        local_path = current_path.__str__() + '/database/' + name
        print("Creating table: ", name)
        pb = ProgressBar(total=100, length=50, fill='█', zfill='-')
        if os.path.isdir(local_path):
            print('Table is already exists!')
        else:
            pb.print_progress_bar(0)
            os.mkdir(local_path)
            pb.print_progress_bar(10)
            title = str(name).title()
            one = title[:-1]
            # M
            with(open(local_path + "/model.py", "w")) as file_model:
                file_model.write(MODEL_TEMPLATE.replace('%title', title).replace("%one", one))
            pb.print_progress_bar(20)
            # S
            with(open(local_path + "/schema.py", "w")) as file_schema:
                file_schema.write(SCHEMA_TEMPLATE.replace('%title', title).replace("%one", one))
            pb.print_progress_bar(30)
            # A
            with(open(local_path + "/actions.py", "w")) as file_actions:
                file_actions.write(ACTIONS_TEMPLATE.replace('%title', title).replace("%one", one))
            pb.print_progress_bar(40)
            # __INIT__
            with(open(local_path + "/__init__.py", "w")) as file_init:
                file_init.write(INIT_TEMPLATE.replace('%title', title).replace("%one", one))
            pb.print_progress_bar(50)
            pb.print_progress_bar(100)
            print("Database template created!")
        input("- Press [Enter] to continue -")


args = sys.argv[1:]
while True:
    if len(args) == 0:
        command = header()
        args = command.split(" ")

    # Commands
    if args[0] == "create":
        command_create(args)
    else:
        break
    args = []

#  ██╗░░░░░██╗███╗░░██╗░██████╗░░░░██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
#  ██║░░░░░██║████╗░██║██╔════╝░░░░██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
#  ██║░░░░░██║██╔██╗██║██║░░██╗░░░░██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
#  ██║░░░░░██║██║╚████║██║░░╚██╗░░░██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
#  ███████╗██║██║░╚███║╚██████╔╝░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
#  ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
#
#  Developed by Yakov V. Panov (C) Ling • Black 2020
#  @site http://ling.black

from sqlalchemy.orm import Session

from database import DatabaseUtils
from database.models import UserGroupModel
from database.schemas import UserGroupCreate


class UserGroupActions:
    """
    The user groups actions utility
    """

    @staticmethod
    def add(db: Session, group: UserGroupCreate):
        """
        Creates the user group
        :param db:
        :param group:
        :return:
        """
        return DatabaseUtils.insert(db, UserGroupModel(title=group.title))

    @staticmethod
    def list(db: Session, offset: int = 0, limit: int = 100):
        """
        Returns all user groups
        :param db:
        :param offset:
        :param limit:
        :return:
        """
        return db.query(UserGroupModel).offset(offset).limit(limit).all()

    @staticmethod
    def get(db: Session, group_id: int):
        """
        Returns the user group by id
        :param db:
        :param group_id:
        :return:
        """
        return db.query(UserGroupModel).filter(UserGroupModel.id == group_id).first()

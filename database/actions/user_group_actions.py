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
    def list(db: Session, offset: int = 0, limit: int = 100, show_removed=False):
        """
        Returns all user groups
        :param show_removed:
        :param db:
        :param offset:
        :param limit:
        :return:
        """
        return DatabaseUtils.limited_results(
            db,
            UserGroupModel,
            offset,
            limit,
            show_removed
        )

    @staticmethod
    def get(db: Session, group_id: int, show_removed=False):
        """
        Returns the user group by id
        :param db:
        :param group_id:
        :param show_removed:
        :return:
        """
        return DatabaseUtils.core_query(
            db.query(UserGroupModel),
            show_removed
        ).filter(UserGroupModel.id == group_id).first()

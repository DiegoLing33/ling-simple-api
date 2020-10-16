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

from database.models import UserGroupModel
from database.usergroup.schema import UserGroupCreate


def get_user_group(db: Session, group_id: int):
    """
    Returns the user group by id
    :param db:
    :param group_id:
    :return:
    """
    return db.query(UserGroupModel).filter(UserGroupModel.id == group_id).first()


def get_user_groups(db: Session, offset: int = 0, limit: int = 100):
    """
    Returns all user groups
    :param db:
    :param offset:
    :param limit:
    :return:
    """
    return db.query(UserGroupModel).offset(offset).limit(limit).all()


def create_user_group(db: Session, group: UserGroupCreate):
    """
    Creates the user group
    :param db:
    :param group:
    :return:
    """
    db_item = UserGroupModel(title=group.title)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

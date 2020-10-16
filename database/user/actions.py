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

from database.models import UserModel
from database.user.schema import UserCreate


def get_user(db: Session, user_id: int):
    """
    Returns the user by id
    :param db:
    :param user_id:
    :return:
    """
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_login(db: Session, login: str) -> UserModel:
    """
    Returns the user by login

    :param db:
    :param login:
    :return:
    """
    return db.query(UserModel).filter(UserModel.login == login).first()


def get_users(db: Session, offset: int = 0, limit: int = 100):
    """
    Returns the users list
    :param db:
    :param offset:
    :param limit:
    :return:
    """
    return db.query(UserModel).offset(offset).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    """
    Creates the user
    :param db:
    :param user:
    :return:
    """
    hashpassword = user.password + "??"
    db_user = UserModel(login=user.login, hashed_password=hashpassword, group_id=user.group_id if user.group_id else 1)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

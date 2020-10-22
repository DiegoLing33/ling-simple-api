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
from hashlib import md5

from sqlalchemy.orm import Session

from database import DatabaseUtils
from database.models import UserModel
from database.schemas import UserCreate


class UserActions:
    """
    The users actions utility
    """

    @staticmethod
    def add(db: Session, user: UserCreate):
        """
        Creates the user
        :param db:
        :param user:
        :return:
        """
        hashpassword = md5(user.password.encode()).hexdigest()
        return DatabaseUtils.insert(db, UserModel(login=user.login, hashed_password=hashpassword,
                                                  group_id=user.group_id if user.group_id else 1))

    @staticmethod
    def list(db: Session, offset: int = 0, limit: int = 100):
        """
        Returns the users list
        :param db:
        :param offset:
        :param limit:
        :return:
        """
        return db.query(UserModel).offset(offset).limit(limit).all()

    @staticmethod
    def get(db: Session, user_id: int):
        """
        Returns the user by id
        :param db:
        :param user_id:
        :return:
        """
        return db.query(UserModel).filter(UserModel.id == user_id).first()

    @staticmethod
    def by_login(db: Session, login: str) -> UserModel:
        """
        Returns the user by login

        :param db:
        :param login:
        :return:
        """
        return db.query(UserModel).filter(UserModel.login == login).first()

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

from fastapi import HTTPException
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
        hash_password = md5(user.password.encode()).hexdigest()
        return DatabaseUtils.insert(
            db,
            UserModel(
                login=user.login,
                hashed_password=hash_password,
                group_id=1
            )
        )

    @staticmethod
    def list(db: Session, offset: int = 0, limit: int = 100, show_removed=False):
        """
        Returns the users list
        :param show_removed:
        :param db:
        :param offset:
        :param limit:
        :return:
        """
        return DatabaseUtils.limited_results(
            db=db,
            model=UserModel,
            offset=offset,
            limit=limit,
            show_removed=show_removed
        )

    @staticmethod
    def get(db: Session, user_id: int, show_removed=False):
        """
        Returns the user by id
        :param show_removed:
        :param db:
        :param user_id:
        :return:
        """
        return DatabaseUtils.core_query(
            db.query(UserModel).filter(UserModel.id == user_id),
            show_removed
        ).first()

    @staticmethod
    def by_login(db: Session, login: str, show_removed=False) -> UserModel:
        """
        Returns the user by login

        :param show_removed:
        :param db:
        :param login:
        :return:
        """
        return DatabaseUtils.core_query(
            db.query(UserModel).filter(UserModel.login == login),
            show_removed
        ).first()

    @staticmethod
    def check(db: Session, user_id: int):
        q = DatabaseUtils.core_query(db.query(UserModel).filter(UserModel.id == user_id))
        if q.count() > 0:
            return True
        raise HTTPException(status_code=404, detail=f"User with user_id [{user_id}] is undefined!")

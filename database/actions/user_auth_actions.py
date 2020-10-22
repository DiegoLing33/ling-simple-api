#  ██╗░░░░░██╗███╗░░██╗░██████╗░░░░██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
#  ██║░░░░░██║████╗░██║██╔════╝░░░░██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
#  ██║░░░░░██║██╔██╗██║██║░░██╗░░░░██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
#  ██║░░░░░██║██║╚████║██║░░╚██╗░░░██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
#  ███████╗██║██║░╚███║╚██████╔╝░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
#  ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
#
#  Developed by Yakov V. Panov (C) Ling • Black 2020
#  @site http://ling.black
from datetime import datetime
from hashlib import md5

from fastapi import HTTPException
from sqlalchemy.orm import Session

from database import DatabaseUtils
from database.actions import UserActions
from database.models import UserAuthModel
from database.schemas import UserAuth


class UserAuthActions:
    """
    The user auth actions
    """

    @staticmethod
    def login(db: Session, login: str, password: str, meta: str):
        """
        Auth logic
        :param db:
        :param login:
        :param password:
        :param meta:
        :return:
        """
        db_user = UserActions.by_login(db, login)
        hashed_psw = md5(password.encode()).hexdigest()
        if db_user and db_user.hashed_password == hashed_psw:
            time: str = datetime.utcnow().__str__()
            login: str = db_user.login
            token = md5((time + login).encode())
            db_obj = UserAuthModel(
                user_id=db_user.id,
                token=token.hexdigest(),
                meta=meta,
            )
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            return db_obj
        else:
            raise HTTPException(status_code=200, detail='Login or password is not correct!')

    @staticmethod
    def get(db: Session, token: str) -> UserAuth:
        """
        Returns the token
        :param db:
        :param token:
        :return:
        """
        db_obj = DatabaseUtils.core_query(db.query(UserAuthModel).filter(UserAuthModel.token == token)).first()
        if db_obj is None:
            raise HTTPException(status_code=201, detail="User's token is undefined!")
        return db_obj

    @staticmethod
    def logout(db: Session, token: str):
        """
        Log out user
        :param db:
        :param token:
        :return:
        """
        db_token = UserAuthActions.get(db, token)
        if db_token:
            db.query(UserAuthModel).filter(UserAuthModel.token == token).update({"state": 0})
            db.commit()
            return {"result": True}
        raise HTTPException(status_code=201, detail="User's token is undefined!")

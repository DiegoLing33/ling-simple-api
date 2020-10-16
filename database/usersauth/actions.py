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

from database.models import UserAuthModel
from database.user.actions import get_user_by_login
from database.usersauth.schema import UserAuth


def user_auth_login(db: Session, login: str, password: str, meta: str):
    """
    Auth logic
    :param db:
    :param login:
    :param password:
    :param meta:
    :return:
    """
    db_user = get_user_by_login(db, login)
    hashed_psw = password + "??"
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


def user_auth_get(db: Session, token: str) -> UserAuth:
    """
    Returns the token
    :param db:
    :param token:
    :return:
    """
    db_obj = db.query(UserAuthModel).filter(UserAuthModel.token == token).filter(UserAuthModel.state == 1).first()
    if db_obj is None:
        raise HTTPException(status_code=201, detail="User's token is undefined!")
    return db_obj


def user_auth_logout(db: Session, token: str):
    """
    Log out user
    :param db:
    :param token:
    :return:
    """
    db_token = user_auth_get(db, token)
    if db_token:
        db.query(UserAuthModel).filter(UserAuthModel.token == token).update({"state": 0})
        db.commit()
        return {"result": True}
    raise HTTPException(status_code=201, detail="User's token is undefined!")

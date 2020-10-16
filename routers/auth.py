#  ██╗░░░░░██╗███╗░░██╗░██████╗░░░░██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
#  ██║░░░░░██║████╗░██║██╔════╝░░░░██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
#  ██║░░░░░██║██╔██╗██║██║░░██╗░░░░██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
#  ██║░░░░░██║██║╚████║██║░░╚██╗░░░██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
#  ███████╗██║██║░╚███║╚██████╔╝░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
#  ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
#
#  Developed by Yakov V. Panov (C) Ling • Black 2020
#  @site http://ling.black

from typing import Optional

from fastapi.params import Header

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from database.usersauth.actions import user_auth_login, user_auth_get, user_auth_logout
from database.usersauth.schema import UserAuth, UserAuthLogin

router = APIRouter()


@router.post("/", response_model=UserAuth)
def auth(body: UserAuthLogin, db: Session = Depends(get_db), user_agent: Optional[str] = Header(None)):
    """
    User auth method. Creates the token
    \f
    :param body:
    :param db:
    :param user_agent:
    :return:
    """
    return user_auth_login(db, body.login, body.password, meta=user_agent)


@router.get("/", response_model=UserAuth)
def me(token: str, db: Session = Depends(get_db)):
    """
    Returns the current user auth data
    \f
    :param token:
    :param db:
    :return:
    """
    return user_auth_get(db, token=token)


@router.get("/logout")
def logout(token: str, db: Session = Depends(get_db)):
    """
    Logouts the user by token

    \f
    :param token:
    :param db:
    :return:
    """
    return user_auth_logout(db, token)

#  ██╗░░░░░██╗███╗░░██╗░██████╗░░░░██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
#  ██║░░░░░██║████╗░██║██╔════╝░░░░██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
#  ██║░░░░░██║██╔██╗██║██║░░██╗░░░░██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
#  ██║░░░░░██║██║╚████║██║░░╚██╗░░░██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
#  ███████╗██║██║░╚███║╚██████╔╝░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
#  ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
#
#  Developed by Yakov V. Panov (C) Ling • Black 2020
#  @site http://ling.black

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic.main import BaseModel
from sqlalchemy.orm import Session

from database.actions import UserActions, UserMetaActions
from database.get_db import get_db
from database.responses import ResponseUsers
from database.schemas import User, UserCreate, UserMeta

router = APIRouter()


class UserMetaCreateBody(BaseModel):
    value: str
    user_id: int


@router.get("/",
            response_model=ResponseUsers,
            summary="Returns the users list",
            description="Returns the users list in offset and limit form"
            )
def users_list(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Returns the users list
    - **offset**: offset of the list
    - **limit**: users on list (max: 400)
    \f
    """
    return UserActions.list(db=db, offset=offset, limit=limit)


@router.get("/id/{user_id}", response_model=User)
def users_list(user_id: int, db: Session = Depends(get_db)):
    """
    Returns the user by login
    - **offset**: offset of the list
    - **limit**: users on list (max: 400)
    \f
    """
    return UserActions.get(db, user_id)


@router.put("/", response_model=User, summary="Creates the new user")
def users_create(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a user with information
    - **login**: the user login
    - **password**: the user password
    \f
    :param user:
    :param db:
    :return:
    """
    db_user = UserActions.by_login(db, login=user.login)
    if db_user:
        raise HTTPException(status_code=400, detail="This login already registered")
    return UserActions.add(db=db, user=user)


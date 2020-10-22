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

from fastapi import Depends, APIRouter, HTTPException

from database import get_db
from database.actions import UserActions, UserMetaActions
from database.responses import ResponseUserMeta
from database.schemas import UserMeta
from routers.users import UserMetaCreateBody

router = APIRouter()


@router.put("/meta/{field}", response_model=UserMeta)
def set_user_meta_value(
        field: str,
        body: UserMetaCreateBody,
        db=Depends(get_db)
):
    """
    Sets the meta value
    \f
    :param body:
    :param field:
    :param db:
    :return:
    """
    db_user = UserActions.get(db, body.user_id)
    if db_user:
        return UserMetaActions.set(db, user_id=body.user_id, field=field, value=body.value)
    else:
        raise HTTPException(status_code=401, detail="User is undefined!")


@router.get("/meta/{field}", response_model=UserMeta)
def get_user_meta_value(
        field: str,
        user_id: int,
        db=Depends(get_db)
):
    """
    Returns the meta value
    \f
    :param user_id:
    :param field:
    :param db:
    :return:
    """
    meta_value = UserMetaActions.get(db, field=field, user_id=user_id)
    if meta_value:
        return meta_value
    raise HTTPException(status_code=401, detail="Meta value is undefined")


@router.get("/meta",
            response_model=ResponseUserMeta,
            summary="Returns the user metadata list",
            description="Returns the user metadata list in offset and limit form"
            )
def get_user_metas(user_id: int, offset: int = 0, limit: int = 100, db=Depends(get_db)):
    """
    Returns all the meta of the user
    \f
    :param user_id:
    :param offset:
    :param limit:
    :param db:
    :return:
    """
    db_user = UserActions.get(db, user_id)
    if db_user:
        return UserMetaActions.list(db, user_id, offset, limit)
    else:
        raise HTTPException(status_code=401, detail="User is undefined!")

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

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.get_db import get_db
from database.usergroup.actions import get_user_groups, create_user_group
from database.usergroup.schema import UserGroup, UserGroupCreate

router = APIRouter()


@router.get("/", response_model=List[UserGroup])
def groups_list(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_user_groups(db=db, offset=offset, limit=limit)


@router.put("/", response_model=UserGroup)
def groups_create(group: UserGroupCreate, db=Depends(get_db)):
    """
    Creates the user group
    :param group: - the user group
    :param db:
    :return:
    """
    return create_user_group(db=db, group=group)

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
from pydantic.main import BaseModel

from database import get_db
from database.client import DataStore
from database.schemas import DataStore


class _DataValueBody(BaseModel):
    value: str


router = APIRouter()


@router.get(
    "/list",
    summary="Returns the list of the store",
    description="All variables stored in data table",
    response_model=List[DataStore]
)
def api_data_list(db=Depends(get_db)):
    return DataStore.list(db)


@router.put(
    "/{field}",
    summary="Sets the value to the field in the store",
    response_model=DataStore
)
def api_data_set(field: str, body: _DataValueBody, db=Depends(get_db)):
    return DataStore.set(db, field=field, value=body.value)


@router.get(
    "/{field}",
    summary="Returns the field's value",
    response_model=DataStore
)
def api_data_get(field: str, db=Depends(get_db)):
    return DataStore.get(db, field=field)


@router.delete(
    "/{field}",
    summary="Deletes the field's value",
)
def api_data_remove(field: str, db=Depends(get_db)):
    return DataStore.remove(db, field=field)

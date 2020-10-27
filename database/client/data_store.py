#  ██╗░░░░░██╗███╗░░██╗░██████╗░░░░██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
#  ██║░░░░░██║████╗░██║██╔════╝░░░░██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
#  ██║░░░░░██║██╔██╗██║██║░░██╗░░░░██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
#  ██║░░░░░██║██║╚████║██║░░╚██╗░░░██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
#  ███████╗██║██║░╚███║╚██████╔╝░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
#  ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
#
#  Developed by Yakov V. Panov (C) Ling • Black 2020
#  @site http://ling.black
from fastapi import HTTPException
from sqlalchemy.orm import Session

from database import DatabaseUtils
from database.models import DataModel


class DataStore:

    @staticmethod
    def list(db: Session):
        """
        Returns all variables
        :param db:
        :return:
        """
        return DatabaseUtils.core_query(db.query(DataModel)).all()

    @staticmethod
    def set(db: Session, field: str, value: str):
        """
        Sets the  value
        :param db:
        :param field:
        :param value:
        :return:
        """
        db_meta = DatabaseUtils.core_query(
            db.query(DataModel).filter(DataModel.field == field)
        )
        if db_meta.count() > 0:
            db_meta.update({"value": value})
            db.commit()
            return db_meta.first()
        return DatabaseUtils.insert(
            db,
            db_item=DataModel(field=field, value=value)
        )

    @staticmethod
    def get(db: Session, field: str):
        """
        Returns the field's value or raises the error
        :param db:
        :param field:
        :return:
        """
        value = DatabaseUtils.core_query(
            db.query(DataModel).filter(DataModel.field == field),
            show_removed=False
        ).first()
        if not value:
            raise HTTPException(status_code=404, detail=f"Stored value [{field}] is undefined!")
        return value

    @staticmethod
    def remove(db: Session, field: str):
        """
        Removes the value
        :param db:
        :param field:
        :return:
        """
        return DatabaseUtils.remove_query(db, db.query(DataModel).filter(DataModel.field == field))

    @staticmethod
    def recover(db: Session, field: str):
        """
        Recovers the value
        :param db:
        :param field:
        :return:
        """
        return DatabaseUtils.recover_query(db, db.query(DataModel).filter(DataModel.field == field))

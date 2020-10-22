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
from database.actions import UserActions
from database.models import UserMetaModel


class UserMetaActions:
    """
    The user meta actions utility
    """

    @staticmethod
    def set(db: Session, user_id: int, field: str, value: str):
        UserActions.check(db, user_id)
        """
        Sets the meta value
        :param db:
        :param user_id:
        :param field:
        :param value:
        :return:
        """
        db_meta = DatabaseUtils.core_query(
            db.query(UserMetaModel).filter(UserMetaModel.user_id == user_id)
                .filter(UserMetaModel.field == field)
        )
        if db_meta.count() > 0:
            db_meta.update({"value": value})
            db.commit()
            return db_meta.first()
        return DatabaseUtils.insert(
            db,
            db_item=UserMetaModel(
                user_id=user_id,
                field=field,
                value=value
            )
        )

    @staticmethod
    def list(db: Session, user_id: int, offset: int = 0, limit: int = 100):
        query = db.query(UserMetaModel).filter(UserMetaModel.user_id == user_id)
        return DatabaseUtils.limited_results_query(
            query,
            offset=offset,
            limit=limit
        )

    @staticmethod
    def get(db: Session, user_id: int, field: str, show_removed=False):
        """
        Returns the user meta value
        :param show_removed:
        :param db:
        :param user_id:
        :param field:
        :return:
        """
        return DatabaseUtils.core_query(
            db.query(UserMetaModel).filter(UserMetaModel.user_id == user_id).filter(UserMetaModel.field == field),
            show_removed
        ).first()

    @staticmethod
    def remove(db: Session, user_id: int, field: str):
        """
        Removes the meta value
        :param db:
        :param user_id:
        :param field:
        :return:
        """
        try:
            return DatabaseUtils.remove_query(
                db,
                db.query(UserMetaModel).filter(UserMetaModel.user_id == user_id, UserMetaModel.field == field)
            )
        except Exception:
            raise HTTPException(detail=f"Meta field [{field}] is undefined (user_id: {user_id})!", status_code=404)

    @staticmethod
    def recover(db: Session, user_id: int, field: str):
        """
        Removes the meta value
        :param db:
        :param user_id:
        :param field:
        :return:
        """
        try:
            return DatabaseUtils.recover_query(
                db,
                db.query(UserMetaModel).filter(UserMetaModel.user_id == user_id, UserMetaModel.field == field)
            )
        except Exception:
            raise HTTPException(detail=f"Meta field [{field}] is undefined (user_id: {user_id})!", status_code=404)

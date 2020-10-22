from sqlalchemy.orm import Session


class DatabaseUtils:
    """
    Database utilities
    """

    @staticmethod
    def insert(db: Session, db_item):
        """
        Inserts item into session db
        :param db:
        :param db_item:
        :return:
        """
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

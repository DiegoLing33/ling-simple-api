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

    @staticmethod
    def limited_results(db, model, offset: int, limit: int):
        query = db.query(model)
        return DatabaseUtils.limited_results_query(query, offset, limit)

    @staticmethod
    def limited_results_query(query, offset: int, limit: int):
        count = query.count()
        items = query.limit(limit).offset(offset).all()
        return {
            "response": {
                "items": items, "count": count
            },
            "request": {"limit": limit, "offset": offset}
        }

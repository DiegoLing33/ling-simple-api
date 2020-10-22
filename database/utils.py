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
    def limited_results(db, model, offset: int, limit: int, show_removed=False):
        query = db.query(model)
        return DatabaseUtils.limited_results_query(query, offset, limit, show_removed)

    @staticmethod
    def limited_results_query(query, offset: int, limit: int, show_removed=False):
        query = DatabaseUtils.core_query(query, show_removed)
        count = query.count()
        items = query.limit(limit).offset(offset).all()
        return {
            "response": {
                "items": items, "count": count
            },
            "request": {"limit": limit, "offset": offset}
        }

    @staticmethod
    def core_query(query, show_removed=False):
        if show_removed:
            return query
        return query.filter_by(state=1)

    @staticmethod
    def remove_query(db, query):
        query = DatabaseUtils.core_query(query)
        if query.count() > 0:
            query.update({'state': 0})
            db.commit()
            return True
        raise Exception("Meta value is undefined")

    @staticmethod
    def recover_query(db, query):
        query = DatabaseUtils.core_query(query, show_removed=True)
        if query.count() > 0:
            query.update({'state': 1})
            db.commit()
            return True
        raise Exception("Meta value is undefined")

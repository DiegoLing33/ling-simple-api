from datetime import datetime

from sqlalchemy import Integer, Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from database.database import Base


class UserModel(Base):
    """
    User model
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String)
    hashed_password = Column(String)
    state = Column(Integer, default=1)

    group_id = Column(Integer, ForeignKey('users_groups.id'))
    group = relationship("UserGroupModel")
    created = Column(DateTime, default=datetime.utcnow)


class UserGroupModel(Base):
    """
    User Group Model
    """
    __tablename__ = "users_groups"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    state = Column(Integer, default=1)


class UserAuthModel(Base):
    """
    User auth model
    """
    __tablename__ = "users_auth"

    id = Column(Integer, primary_key=True, index=True)
    created = Column(DateTime, default=datetime.utcnow)
    state = Column(Integer, default=1)
    token = Column(String)
    meta = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("UserModel")

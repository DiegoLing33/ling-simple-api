#  ██╗░░░░░██╗███╗░░██╗░██████╗░░░░██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
#  ██║░░░░░██║████╗░██║██╔════╝░░░░██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
#  ██║░░░░░██║██╔██╗██║██║░░██╗░░░░██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
#  ██║░░░░░██║██║╚████║██║░░╚██╗░░░██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
#  ███████╗██║██║░╚███║╚██████╔╝░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
#  ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
#
#  Developed by Yakov V. Panov (C) Ling • Black 2020
#  @site http://ling.black

from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base
from database.core.models import CoreModel


#
# +-----------------------------------------------+
# |                   Users                       |
# +-----------------------------------------------+
#

class UserModel(Base, CoreModel):
    """
    User model
    """
    __tablename__ = "users"

    login = Column(String)
    hashed_password = Column(String)

    group_id = Column(Integer, ForeignKey('users_groups.id'))
    group = relationship("UserGroupModel")

    meta = relationship("UserMetaModel", back_populates="user")


class UserGroupModel(Base, CoreModel):
    """
    User Group Model
    """
    __tablename__ = "users_groups"

    title = Column(String)


#
# +-----------------------------------------------+
# |              Users Auth                       |
# +-----------------------------------------------+
#


class UserAuthModel(Base, CoreModel):
    """
    User auth model
    """
    __tablename__ = "users_auth"
    token = Column(String)
    meta = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("UserModel")


#
# +-----------------------------------------------+
# |                 Users Meta                    |
# +-----------------------------------------------+
#

class UserMetaModel(Base, CoreModel):
    """
    User meta model
    """
    __tablename__ = "users_meta"
    user_id = Column(Integer, ForeignKey("users.id"))
    field = Column(String)
    value = Column(String)

    user = relationship("UserModel", back_populates="meta")

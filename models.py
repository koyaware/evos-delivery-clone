from gino import Gino
from sqlalchemy import Column, Boolean, String, BigInteger, ForeignKey

db = Gino()


class Users(db.Model):

    __tablename__ = "users"

    tg_id = Column(BigInteger(), primary_key=True)
    is_user = Column(Boolean(), default=True)


class Products(db.Model):

    __tablename__ = "products"

    Id = Column(BigInteger(), primary_key=True)
    name = Column(String(120), unique=True)
    photo_url = Column(String, unique=True)
    desc = Column(String(120))


class Trash(db.Model):

    __tablename__ = "trash"

    Id = Column(BigInteger(), primary_key=True)
    user_id = Column(ForeignKey("users.tg_id"))
    products_id = Column(ForeignKey("products.Id"))
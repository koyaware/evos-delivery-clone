from gino import Gino
from sqlalchemy import Column, Boolean, String, BigInteger, ForeignKey, DateTime

db = Gino()


class Users(db.Model):

    __tablename__ = "users"

    tg_id = Column(BigInteger(), primary_key=True)
    is_user = Column(Boolean(), default=True)
    phone_number = Column(String(128))
    location_latitude = Column(String(256))
    location_longitude = Column(String(256))


class Products(db.Model):

    __tablename__ = "products"

    Id = Column(BigInteger(), primary_key=True)
    name = Column(String(128), unique=True)
    photo_url = Column(String, unique=True)
    desc = Column(String(1028))
    price = Column(BigInteger(), default=None)


class Cart(db.Model):

    __tablename__ = "cart"

    Id = Column(BigInteger(), primary_key=True)
    user_id = Column(ForeignKey("users.tg_id"))


class CartProducts(db.Model):

    __tablename__ = "cart products"

    Id = Column(BigInteger(), primary_key=True)
    cart_id = Column(ForeignKey("cart.Id"))
    products_id = Column(ForeignKey("products.Id"))
    amount = Column(BigInteger(), default=1)


class OrderHistory(db.Model):

    __tablename__ = "order history"

    Id = Column(BigInteger(), primary_key=True)
    cart_products = Column(ForeignKey("cart products.Id"))
    completed = Column(Boolean(), default=False)
    user_id = Column(ForeignKey("users.tg_id"))
    order_date = Column(DateTime())
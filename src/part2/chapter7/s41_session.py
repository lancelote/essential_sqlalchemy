from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship, sessionmaker

engine = create_engine('sqlite:///:memory:')  # Add echo=True to see raw database log
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Cookie(Base):
    __tablename__ = 'cookies'

    cookie_id = Column(Integer(), primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12, 2))

    def __repr__(self):
        return ("Cookie("
                "    cookie_name='{self.cookie_name}',"
                "    cookie_recipe_url='{self.cookie_recipe_url}',"
                "    cookie_sku='{self.cookie_sku}',"
                "    quantity={self.quantity},"
                "    unit_cost={self.unit_cost}"
                ")".format(self=self))


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    email_address = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    password = Column(String(25), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return ("User("
                "    username='{self.username}',"
                "    email_address='{self.email_address}',"
                "    phone='{self.phone}',"
                "    password='{self.password}'"
                ")".format(self=self))


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.user_id'))
    user = relationship('User', backref=backref('orders', order_by=order_id))

    def __repr__(self):
        return ('Order('
                '    user_id={self.user_id},'
                '    shipped={self.shipped},'
                ')'.format(self=self))


class LineItem(Base):
    __tablename__ = 'line_items'

    line_item_id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.order_id'))
    cookie_id = Column(Integer(), ForeignKey('cookies.cookie_id'))
    quantity = Column(Integer())
    extended_cost = Column(Numeric(12, 2))
    order = relationship('Order', backref=backref('line_items', order_by=line_item_id))
    cookie = relationship('Cookie', uselist=False, order_by=line_item_id)

    def __repr__(self):
        return ("LineItems("
                "    order_id={self.order_id},"
                "    cookie_id={self.cookie_id},"
                "    quantity={self.quantity},"
                "    extended_cost={self.extended_cost}"
                ")".format(self=self))


Base.metadata.create_all(engine)

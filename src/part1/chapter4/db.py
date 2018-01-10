from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, MetaData, Numeric, String, Table, create_engine


class DataAccessLayer:
    connection = None
    engine = None
    connection_string = None
    metadata = MetaData()
    cookies = Table(
        'cookies', metadata,
        Column('cookie_id', Integer(), primary_key=True),
        Column('cookie_name', String(50), index=True),
        Column('cookie_recipe_url', String(255)),
        Column('cookie_sku', String(55)),
        Column('quantity', Integer()),
        Column('unit_cost', Numeric(12, 2))
    )

    users = Table(
        'users', metadata,
        Column('user_id', Integer(), primary_key=True),
        Column('customer_number', Integer(), autoincrement=True),
        Column('username', String(15), nullable=False, unique=True),
        Column('email_address', String(255), nullable=False),
        Column('phone', String(20), nullable=False),
        Column('password', String(25), nullable=False),
        Column('created_on', DateTime(), default=datetime.now),
        Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
    )

    orders = Table(
        'orders', metadata,
        Column('order_id', Integer()),
        Column('user_id', ForeignKey('users.user_id')),
        Column('shipped', Boolean(), default=False)
    )

    line_items = Table(
        'line_items', metadata,
        Column('line_items_id', Integer(), primary_key=True),
        Column('order_id', ForeignKey('orders.order_id')),
        Column('cookie_id', ForeignKey('cookies.cookie_id')),
        Column('quantity', Integer()),
        Column('extended_cost', Numeric(12, 2))
    )

    def db_init(self, conn_string):
        self.engine = create_engine(conn_string or self.connection_string)
        self.metadata.create_all(self.engine)
        self.connection = self.engine.connect()


data_access_layer = DataAccessLayer()

from sqlalchemy import Table, MetaData, PrimaryKeyConstraint, Column, Integer, \
    UniqueConstraint, String, Numeric, CheckConstraint

metadata = MetaData()

users = Table(
    'users', metadata,
    Column('user_id', Integer()),
    Column('username', String(15), nullable=False),
    PrimaryKeyConstraint('user_id', name='user_pk'),
    UniqueConstraint('username', name='uix_username')
)

cookies = Table(
    'cookies', metadata,
    Column('unit_cost', Numeric(12, 2)),
    CheckConstraint('unit_cost >= 0.00', name='unit_cost_positive')
)

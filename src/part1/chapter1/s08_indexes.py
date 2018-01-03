from sqlalchemy import Table, Column, Integer, Numeric, String, MetaData, Index

metadata = MetaData()

cookies = Table(
    'cookies', metadata,
    Column('cookie_id', Integer(), primary_key=True),
    Column('cookie_name', String(50), index=True),
    Column('cookie_recipe_url', String(255)),
    Column('cookie_sku', String(55)),
    Column('quantity', Integer()),
    Column('unit_cost', Numeric(12, 2)),
)

Index('ix_test', cookies.c.cookie_sku, cookies.c.cookie_name)

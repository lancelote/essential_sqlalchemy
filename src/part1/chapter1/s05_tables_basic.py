from sqlalchemy import Table, Column, Integer, Numeric, String, MetaData

metadata = MetaData()

cookies = Table(
    'cookies', metadata,
    Column('cookie_id', Integer(), primary_key=True),
    Column('cookie_name', String(50), index=True),
    Column('cookie_recipe_url', String(255)),
    Column('cookie_sku', String(55)),
    Column('quantity', Integer()),
    Column('unit_cost', Numeric(12, 2)),  # 11 digit long with 2 decimal places
)

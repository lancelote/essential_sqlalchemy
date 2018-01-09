from sqlalchemy import Column, Integer, MetaData, Numeric, String, Table, create_engine


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

    def db_init(self, connection_string):
        self.engine = create_engine(connection_string or self.connection_string)
        self.metadata.create_all(self.engine)
        self.connection = self.engine.connect()


data_access_layer = DataAccessLayer()

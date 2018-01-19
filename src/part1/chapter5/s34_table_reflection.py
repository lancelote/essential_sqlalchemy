from sqlalchemy import MetaData, Table, create_engine, select

metadata = MetaData()
engine = create_engine('sqlite:///../../../dbs/Chinook_Sqlite.sqlite')

artist = Table('Artist', metadata, autoload=True, autoload_with=engine)
assert artist.columns.keys() == ['ArtistId', 'Name']

selection = select([artist]).limit(10)
first_10_records = engine.execute(selection).fetchall()
assert first_10_records[0] == (1, 'AC/DC')

album = Table('Album', metadata, autoload=True, autoload_with=engine)
# print(metadata.tables['Album'])
#
#    Table('Album',
#        MetaData(bind=None),
#        Column('AlbumId', INTEGER(), table=<Album>, primary_key=True, nullable=False),
#        Column('Title', NVARCHAR(length=160), table=<Album>, nullable=False),
#        Column('ArtistId', INTEGER(), ForeignKey('Artist.ArtistId'), table=<Album>, nullable=False), schema=None)
#    )

# print(album.foreign_keys)
#
#    {ForeignKey('Artist.ArtistId')}

assert str(artist.join(album)) == '"Artist" JOIN "Album" ON "Artist"."ArtistId" = "Album"."ArtistId"'

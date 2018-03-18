from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

Base = automap_base()
engine = create_engine('sqlite:///../../../dbs/Chinook_Sqlite.sqlite')
session = Session(engine)

# Reflect the database
Base.prepare(engine, reflect=True)
assert Base.classes.keys() == [
    'Album',
    'Artist',
    'Customer',
    'Employee',
    'Genre',
    'Invoice',
    'InvoiceLine',
    'Track',
    'MediaType',
    'Playlist'
]

Artist = Base.classes.Artist
Album = Base.classes.Album

artists = [(artist.ArtistId, artist.Name) for artist in session.query(Artist).limit(3)]
assert artists == [(1, 'AC/DC'), (2, 'Accept'), (3, 'Aerosmith')]

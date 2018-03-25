# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Index, Integer, Numeric, Table, Unicode
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Album(Base):
    __tablename__ = 'Album'

    AlbumId = Column(Integer, primary_key=True, unique=True)
    Title = Column(Unicode(160), nullable=False)
    ArtistId = Column(ForeignKey('Artist.ArtistId'), nullable=False, index=True)

    Artist = relationship('Artist')


class Artist(Base):
    __tablename__ = 'Artist'

    ArtistId = Column(Integer, primary_key=True, unique=True)
    Name = Column(Unicode(120))


class Customer(Base):
    __tablename__ = 'Customer'

    CustomerId = Column(Integer, primary_key=True, unique=True)
    FirstName = Column(Unicode(40), nullable=False)
    LastName = Column(Unicode(20), nullable=False)
    Company = Column(Unicode(80))
    Address = Column(Unicode(70))
    City = Column(Unicode(40))
    State = Column(Unicode(40))
    Country = Column(Unicode(40))
    PostalCode = Column(Unicode(10))
    Phone = Column(Unicode(24))
    Fax = Column(Unicode(24))
    Email = Column(Unicode(60), nullable=False)
    SupportRepId = Column(ForeignKey('Employee.EmployeeId'), index=True)

    Employee = relationship('Employee')


class Employee(Base):
    __tablename__ = 'Employee'

    EmployeeId = Column(Integer, primary_key=True, unique=True)
    LastName = Column(Unicode(20), nullable=False)
    FirstName = Column(Unicode(20), nullable=False)
    Title = Column(Unicode(30))
    ReportsTo = Column(ForeignKey('Employee.EmployeeId'), index=True)
    BirthDate = Column(DateTime)
    HireDate = Column(DateTime)
    Address = Column(Unicode(70))
    City = Column(Unicode(40))
    State = Column(Unicode(40))
    Country = Column(Unicode(40))
    PostalCode = Column(Unicode(10))
    Phone = Column(Unicode(24))
    Fax = Column(Unicode(24))
    Email = Column(Unicode(60))

    parent = relationship('Employee', remote_side=[EmployeeId])


class Genre(Base):
    __tablename__ = 'Genre'

    GenreId = Column(Integer, primary_key=True, unique=True)
    Name = Column(Unicode(120))


class Invoice(Base):
    __tablename__ = 'Invoice'

    InvoiceId = Column(Integer, primary_key=True, unique=True)
    CustomerId = Column(ForeignKey('Customer.CustomerId'), nullable=False, index=True)
    InvoiceDate = Column(DateTime, nullable=False)
    BillingAddress = Column(Unicode(70))
    BillingCity = Column(Unicode(40))
    BillingState = Column(Unicode(40))
    BillingCountry = Column(Unicode(40))
    BillingPostalCode = Column(Unicode(10))
    Total = Column(Numeric(10, 2), nullable=False)

    Customer = relationship('Customer')


class InvoiceLine(Base):
    __tablename__ = 'InvoiceLine'

    InvoiceLineId = Column(Integer, primary_key=True, unique=True)
    InvoiceId = Column(ForeignKey('Invoice.InvoiceId'), nullable=False, index=True)
    TrackId = Column(ForeignKey('Track.TrackId'), nullable=False, index=True)
    UnitPrice = Column(Numeric(10, 2), nullable=False)
    Quantity = Column(Integer, nullable=False)

    Invoice = relationship('Invoice')
    Track = relationship('Track')


class MediaType(Base):
    __tablename__ = 'MediaType'

    MediaTypeId = Column(Integer, primary_key=True, unique=True)
    Name = Column(Unicode(120))


class Playlist(Base):
    __tablename__ = 'Playlist'

    PlaylistId = Column(Integer, primary_key=True, unique=True)
    Name = Column(Unicode(120))

    Track = relationship('Track', secondary='PlaylistTrack')


t_PlaylistTrack = Table(
    'PlaylistTrack', metadata,
    Column('PlaylistId', ForeignKey('Playlist.PlaylistId'), primary_key=True, nullable=False),
    Column('TrackId', ForeignKey('Track.TrackId'), primary_key=True, nullable=False, index=True),
    Index('IPK_PlaylistTrack', 'PlaylistId', 'TrackId', unique=True)
)


class Track(Base):
    __tablename__ = 'Track'

    TrackId = Column(Integer, primary_key=True, unique=True)
    Name = Column(Unicode(200), nullable=False)
    AlbumId = Column(ForeignKey('Album.AlbumId'), index=True)
    MediaTypeId = Column(ForeignKey('MediaType.MediaTypeId'), nullable=False, index=True)
    GenreId = Column(ForeignKey('Genre.GenreId'), index=True)
    Composer = Column(Unicode(220))
    Milliseconds = Column(Integer, nullable=False)
    Bytes = Column(Integer)
    UnitPrice = Column(Numeric(10, 2), nullable=False)

    Album = relationship('Album')
    Genre = relationship('Genre')
    MediaType = relationship('MediaType')

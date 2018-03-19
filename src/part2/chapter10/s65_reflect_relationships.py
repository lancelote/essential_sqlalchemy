from src.part2.chapter10.s64_reflection import Artist, session

artist = session.query(Artist).first()
albums = [album.Title for album in artist.album_collection]
assert albums == ['For Those About To Rock We Salute You', 'Let There Be Rock']

import sqlite3


with sqlite3.connect('music_db.sqlite') as con:
    genre = input()
    cur = con.cursor()
    result = cur.execute(f"""Select DISTINCT artist.Name from track
inner join Genre on track.GenreId = genre.GenreId and genre.Name = '{genre}'
left join album on album.AlbumId = track.AlbumId
left join artist on artist.ArtistId = album.ArtistId
order by artist.Name""").fetchall()
    for elem in result:
        print(elem[0])

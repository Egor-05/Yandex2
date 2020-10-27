import sqlite3


with sqlite3.connect('music_db.sqlite') as con:
    name = input()
    cur = con.cursor()
    result = cur.execute(f"""SELECT DISTINCT Name FROM Track 
    WHERE albumid in (SELECT albumid FROM Album 
    WHERE artistid = (SELECT artistid FROM Artist WHERE name = '{name}')) order by name""").fetchall()
    for elem in result:
        print(elem[0])

import sqlite3


db_name = input()
with sqlite3.connect(db_name) as con:
    cur = con.cursor()
    result = cur.execute("""SELECT title FROM Genres WHERE id in 
    (SELECT DISTINCT genre FROM Films WHERE year BETWEEN 2010 AND 2011)""").fetchall()
    for elem in result:
        print(elem[0])

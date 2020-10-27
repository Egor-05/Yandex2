import sqlite3


db_name = input()
with sqlite3.connect(db_name) as con:
    cur = con.cursor()
    result = cur.execute("""SELECT DISTINCT title FROM Films 
    WHERE duration <= 85""").fetchall()
    for elem in result:
        print(elem[0])

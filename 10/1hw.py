import sqlite3


db_name = input()
with sqlite3.connect(db_name) as con:
    cur = con.cursor()
    result = cur.execute("""SELECT DISTINCT title FROM Films WHERE genre = 4 
    AND year BETWEEN 1995 AND 2000""").fetchall()
    for elem in result:
        print(elem[0])

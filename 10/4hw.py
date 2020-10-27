import sqlite3


db_name = input()
with sqlite3.connect(db_name) as con:
    cur = con.cursor()
    result = cur.execute("""SELECT title FROM Films WHERE title like '%Астерикс%' 
    AND title not like '%Обеликс%'""").fetchall()
    for elem in result:
        print(elem[0])

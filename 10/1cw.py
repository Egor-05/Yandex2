import sqlite3


db_name = input()
with sqlite3.connect(db_name) as con:
    cur = con.cursor()
    result = cur.execute("""SELECT title FROM Films 
    WHERE genre = (SELECT id FROM genres 
    WHERE title = 'музыка' or title = 'анимация') AND year >= 1997""").fetchall()
    for elem in result:
        print(elem[0])

import sqlite3


def get_result(name):
    with sqlite3.connect(name) as con:
        cur = con.cursor()
        cur.execute("""DELETE from films
                       where title like 'Я%а'""").fetchall()
        con.commit()


get_result('films_db.sqlite')
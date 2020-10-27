import sqlite3


def get_result(name):
    with sqlite3.connect(name) as con:
        cur = con.cursor()
        cur.execute("""UPDATE films
                       SET duration = duration / 3
                       WHERE year = 1973""").fetchall()
        con.commit()

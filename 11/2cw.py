import sqlite3


def get_result(name):
    with sqlite3.connect(name) as con:
        cur = con.cursor()
        cur.execute("""UPDATE films
                       SET duration = '42'
                       WHERE duration = ''""").fetchall()
        con.commit()
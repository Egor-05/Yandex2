import sqlite3


def get_result(name):
    with sqlite3.connect(name) as con:
        cur = con.cursor()
        cur.execute("""DELETE from films
                       where genre = (SELECT id FROM genres 
                       WHERE title = 'боевик') AND duration >= 90 """).fetchall()
        con.commit()

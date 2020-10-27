import sqlite3


def get_result(name):
    with sqlite3.connect(name) as con:
        cur = con.cursor()
        cur.execute("""UPDATE films
                       SET duration = 100
                       WHERE genre = (SELECT id FROM genres 
                       WHERE title = 'мюзикл') AND duration > 100""").fetchall()
        con.commit()

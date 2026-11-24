import sqlite3

class Games:
    def __init__(self):
        self.file = "vgsales.db"

    def __enter__(self):
        self.con = sqlite3.connect(self.file)
        return self.con

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.close()


with Games() as cur:
    res = cur.execute('select 1')
    print(res.fetchone())


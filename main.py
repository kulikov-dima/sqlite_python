import sqlite3

platform = input("Введите платформу: ")

con = sqlite3.connect("vgsales.db")
cur = con.execute("SELECT * FROM games WHERE Platform = ?", (platform,))
result = cur.fetchall()

for game in result:
    print(game)

con.close()
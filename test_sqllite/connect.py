import sqlite3

connection = sqlite3.connect("Chinook_Sqlite.sqlite")

sql = "SELECT * FROM Album"

r = connection.execute(sql)

for row in r.fetchall():
    print(row)

connection.close()

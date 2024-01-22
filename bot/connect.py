import sqlite3

connect = sqlite3.connect('../db.sqlite3')
cursor = connect.cursor()

print(connect)

cursor.execute("SELECT * FROM ProductAPP_katalogmodel")

catalogs = cursor.fetchall()

connect.close()
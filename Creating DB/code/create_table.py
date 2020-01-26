import sqlite3
connection=sqlite3.connect('data.db')
cursor=connection.cursor()
create_table="create table if not exists users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)


create_table="create table if not exists items (name text, price real)"
cursor.execute(create_table)
#cursor.execute("insert into items values('airpods',160.77)")


selectQ="SELECT * FROM items"
for row in cursor.execute(selectQ):
	print(row)

connection.commit()
connection.close()
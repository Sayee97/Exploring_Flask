import sqlite3
connection=sqlite3.connect('data.db')
cursor=connection.cursor()  #run query and access it

create_table="CREATE TABLE users (id int,username text, password text)" #schema

cursor.execute(create_table)

#user=

insert_query="INSERT INTO users VALUES(?,?,?)"
#cursor.execute(insert_query,user)
######### For inserting multiple users 
users=[(1,'jose','asdf'),('2','sam','wer'),('3','sayee','wer')]
cursor.executemany(insert_query,users)

 
selectQ="SELECT * FROM users"
for row in cursor.execute(selectQ):
	print(row)
connection.commit()
connection.close()
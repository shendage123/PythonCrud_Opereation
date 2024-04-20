import mysql.connector as myconn
mydb=myconn.connect(host="localhost",user="root",password="tiger",database="e_Adhar")
db_cursor=mydb.cursor()
db_cursor.execute("create table e_Adhar.Adhar_portal(id int,name varchar(30),addr varchar(30),mob int, age int) ")
print("Table is Created")
import mysql.connector as myconn
mydb=myconn.connect(host="localhost",user="root",password="tiger")
db_cursor=mydb.cursor()
db_cursor.execute("create database E_Adhar")
print("Adhar is database is created")
import mysql.connector as myconn
mydb=myconn.connect(host="localhost",user="root",password="tiger",database="E_Adhar")
db_cursor=mydb.cursor()
db_cursor.execute("select * from E_Adhar.Adhar_Portal")
for i in db_cursor.fetchall():
    print(i)
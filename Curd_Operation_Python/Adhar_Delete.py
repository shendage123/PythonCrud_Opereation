import mysql.connector as myconn
mydb=myconn.connect(host="localhost",user="root",password="tiger",database="E_Adhar")
db_cursor=mydb.cursor()
db_delete=("delete from E_Adhar.Adhar_Portal  where id=%s ")
value=(6,)
db_cursor.execute(db_delete,value)
mydb.commit()
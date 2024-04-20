import mysql.connector as myconn
mydb=myconn.connect(host="localhost",user="root",password="tiger",database="E_Adhar")
db_cursor=mydb.cursor()
db_update="update E_Adhar.Adhar_portal set name=%s where id=%s"
db_value=("Rahul",2)
db_cursor.execute(db_update,db_value)
mydb.commit()
print("Update the database")
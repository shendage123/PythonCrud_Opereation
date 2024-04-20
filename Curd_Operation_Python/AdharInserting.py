import mysql.connector as myconn
mydb=myconn.connect(host="localhost",user="root",password="tiger",database="E_Adhar")
db_cursor=mydb.cursor()
db_insert="insert into Adhar_portal(id,name,addr,mob,age) values(%s,%s,%s,%s,%s)"
db_list=[(1,"Shubham","Pune",947847,22),(2,"Sejal","Kolhapur",907847,21),(3,"Narayan","Nashik",946847,26),(4,"priya","Pahur",9057847,25),(5,"Radhika","U.S",947847,22),(6,"Gopal","Pune",947897,22)]
db_cursor.executemany(db_insert,db_list)
mydb.commit()
print("Data is inserted")
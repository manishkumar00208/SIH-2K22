import mysql.connector as c

mydb = c.connect(host="LAPTOP-631I4VEI", user="manish", passwd="1234", database="aadhardetails")

mycursor = mydb.cursor()

mycursor.execute("select * from students")

for i in mycursor:
    print(i)
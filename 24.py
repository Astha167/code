#WAP to connect with database and delete the record of entered employee number.
import mysql.connector as x
con=x.connect(host="localhost",user="root",passwd="Bunny@605",database="employee")
c=con.cursor()
n=int(input("Enter employee id whose record is to be deleted"))
s="Delete from record where emp_id={}".format(n)
c.execute(s)
con.commit()
con.close()
#Astha Kumari,12-E,roll=15

#WAP to connect with database and update the employee record of entered empno
import mysql.connector as x
con=x.connect(host='localhost',user='root',passwd='Bunny@605',database='employee')
c=con.cursor()
c.execute('Select*from record')
d=c.fetchall()
n=int(input("enter employee no whose record is to be updated"))
sal=int(input("Enter required salary"))
s="Update record set salary={} where emp_id={}".format(sal,n)
c.execute(s)
con.commit()
con.close()
#Astha Kumari,12-E,roll-15

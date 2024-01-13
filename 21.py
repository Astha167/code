#WAP to connect with database and store record of employee and display records
import mysql.connector as x
con=x.connect(host="localhost",user="root",passwd="Bunny@605",database="employee")
c=con.cursor()
c.execute("Create table record(emp_id int,emp_name char(40),salary int)")
con.commit()

#Storing record
s="Insert into record (emp_id,emp_name,salary)Values({},'{}',{})".format (100,'Nikita Mehra',89000)
c.execute(s)
con.commit()
s1="Insert into record (emp_id,emp_name,salary)Values({},'{}',{})".format(102,'Ramesh Oberoi',900000)
c.execute(s1)
con.commit()
s2="Insert into record (emp_id,emp_name,salary)Values({},'{}',{})".format(103,'Priya Mukherjee',780000)
c.execute(s2)
con.commit()
s3="Insert into record (emp_id,emp_name,salary)Values({},'{}',{})".format(104,'Pallavi Kapoor',340000)
c.execute(s3)
con.commit()
s4="Insert into record (emp_id,emp_name,salary)Values({},'{}',{})".format(105,'Roshan Mishra',450000)
c.execute(s4)
con.commit()

#Display Record
c.execute("Select*from record")
data=c.fetchall()
for i in data:
    print(i)
con.close()

#Astha Kumari,12-E,roll-15

        

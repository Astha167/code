#WAP to connect with database and search employee number in table employee and display record, if emp no not found display appropriate message.
import mysql.connector as m
con=m.connect(host='localhost',user='root',passwd='Bunny@605',database='employee')
c=con.cursor()
print('******************************************************************************')
c.execute("Select*from employee")
data=c.fetchall()
while True:
    r=int(input('enter emp_id(100-105):'))
    c=0
    for i in data:
        if i[0]==r:
            e_name=i[1]
            e_sal=i[2]
            print(r,e_name,e_sal)
            c=c+1
            break
    if c==0:
        print("Record not found")
    ch=input("Do you want to continue?y/n")
    if ch in 'Nn':
        break


#Astha Kumari,12-E,roll-15
    
        

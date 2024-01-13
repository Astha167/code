

print("School Management System")

import mysql.connector as m
con=m.connect(host='localhost',user='root',passwd='Bunny@605')

#To create a cursor object for executing mysql statements

c=con.cursor() #where c is cursor object

#to create database

#c.execute("Create database school_management_system")
                                                                                        #Teacher Management

def teacher():
    print("Welcome to teacher management sector")
    print('************************************************************************************************************')
    
    #Creating table to store records of the teacher
    
    c.execute("Use school_management_system")
    #c.execute("Create table teacher( Id int, Name char(70), Salary int,Age int, experience int,department  char(40))")
    
    #Accepting records
     
    def rec():
        while True:
            i=int(input("Enter 4 digit id number :"))
            N=input("Enter teacher's name:")
            sal=int(input("Enter salary:"))
            ag=int(input("Enter teacher's age:"))
            e=int(input("Enter teaching experience:"))
            d=input("Enter department")      
            s="Insert into teacher(Id,name,salary,age,experience,department)values({},'{}',{},{},{},'{}')".format(i,N,sal,ag,e,d)
            c.execute(s)
            con.commit()
            z=input("Wanna enter more records?y/n")
            if z in 'Nn':
                break
        print("Records has been inserted successfully")
        print('************************************************************************************************************')
    
     #Remove a record of teacher
    
    def remove():
        while True:
            i=int(input("Enter id of the teacher whose record is to be removed"))
            r="Delete from teacher where Id={}".format(i)
            c.execute(r)
            con.commit()
            z=input("Wanna delete more rec?y/n")
            if z in 'Nn':
                break
        print("Record deletion successfull")
        print('************************************************************************************************************')
         
     #To search records
     
    def search():
        k=int(input("Enter id to be searched"))
        c.execute("Select*from teacher")
        data=c.fetchall()
        w=0
        print("Required record:")
        for i in data:
            if i[0]==k:
                n=i[1]
                s=i[2]
                a=i[3]
                e=i[4]
                d=i[5]
                print(k,n,s,a,e,d)
                w=w+1
                break
        if w==0:
            print("Record Not Found")
        print('************************************************************************************************************')    
      
    #to display records
    
    def show():
        c.execute("Select*from teacher")
        d=c.fetchall()
        for i in d:
            print(i)
        print('************************************************************************************************************')    
       
    # to update salary
    
    def update_sal():
        while True:
            o=int(input("Enter id whose sal is to be updated"))
            sal=int(input("Enter new salary:"))
            u="Update teacher set salary={} where id={}".format(sal,o)
            c.execute(u)
            m=input("Would you like to continue?y/n")
            if m in 'Nn':
                break
        print("Table updation successful")
        print('************************************************************************************************************')
      
    #To display teachers name department wise
   
    def dept():
        while True:
            d=input("Enter department whose record is to be displayed")
            p="select * from teacher where department='{}' ".format(d)
            c.execute(p)
            l=c.fetchall()
            for i in l:
                print(i)
            r=input("wanna continue?y/n")
            if r in 'Nn':
                break
            print('************************************************************************************************************')

    print('1.Accept records')
    print('2.delete records')
    print('3.Search records')
    print('4.show records')
    print('5.update salary')
    print('6.show department wise records')
    
    while True:
        q=int(input("Enter your choice"))
        if q==1:
            rec()
        elif q==2:
            remove()
        elif q==3:
            search()
        elif q==4:
            show()
        elif q==5:
            update_sal()
        elif q==6:
            dept()
        else:
            print("Invalid choice")
        g=input("Wanna continue?y/n")
        if g in 'Nn':
            break

           
        
                                          #Student Management
         
def student():
    print("welcome to Student Management Sector")
    print('************************************************************************************************************')
    
    #Creating a table for storing records of student
    
    c.execute("Use school_management_system")
    c.execute("Create table student(Roll int,name char(30),class char(20),age int,adm_no int, city char(40) ,fee int)")
    
    #inserting values in student table
    
    def insert():
        while True:
            r=int(input("Enter roll:"))
            n=input("Enter name:")
            a=int(input("Enter age:"))
            cl=input("Enter class :")
            adm=int(input("Enter adm no:"))
            city=input("enter city")
            f=int(input("Enter fees"))
            s="Insert into student (roll,name,age,class,adm_no,city,fee)values({},'{}',{},'{}',{},'{}',{})".format(r,n,a,cl,adm,city,f)
            c.execute(s)
            con.commit()
            ch=input("Want to insert more records?y/n")
            if ch in 'Nn':
                break
        print("Successfully inserted records in student table")
        print('************************************************************************************************************')
           
    # to display records of all students
    
    def display():
        c.execute("Select*from student")
        rec=c.fetchall()
        print("Records of student table are:")
        for i in rec:
            print(i)
        print('************************************************************************************************************')
     
    #to search records of a student whose adm_no is known
    def search():
        c.execute("Select*from student")
        d=c.fetchall()
        while True:
            ad=int(input("Enter adm_no of student whose record is to be searched:"))
            z=0
            for  i in d:
                if i[4]==ad:
                    r=i[0]
                    n=i[1]
                    a=i[2]
                    cl=i[3]
                    ci=i[5]
                    f=i[6]
                    print("Here's the record for adm_no",ad,":")
                    print(r,n,a,cl,ci,f)
                    print('************************************************************************************************************')
                    z=z+1
                    break
            if z==0:
                print("Record not found")
            j=input("Wanna continue?y/n")
            if j in'Nn':
                break
                    
   #to update class of student
     
    def update_class():
         while True:
             r=int(input("Enter roll:"))
             cl=input("Enter class of student:")
             u="Update student set class='{}' Where roll={}".format(cl,r)
             c.execute(u)
             con.commit()
             ch=input("Want to update class of more students?y/n")
             if ch in 'Nn':
                 break
             print("Class is updated successfully")
             print('************************************************************************************************************')
            
    #To delete a record
    def delete():
         while True:
             r=int(input("Enter roll of student whose record is to be deleted"))
             d="Delete from student where roll={}".format(r)
             c.execute(d)
             con.commit()
             ch=input("Wanna delete more records?y/n")
             if ch in 'Nn':
                 break
             print("Deletion of record is successful")
             print('************************************************************************************************************')
             
    #count distinct records
    def count_dis():
         c.execute("select count(distinct(city))from student")
         d=c.fetchall()
         print('The count of distinct(city) records:')
         for i in d:
             print(i)
             break
             print('************************************************************************************************************')
        
     #display distinct city
            
    def distinct_display():
         c.execute("Select distinct(city) from student")
         d=c.fetchall()
         print("Distinct city:")
         for i in d:
             print(i)
         print('************************************************************************************************************')
        
     #Display records where name starts with the entered char by the user
      
    def dis_char():
         while True:
             n=input('Enter')
             st="Select *from student where name like'{}%'".format(n)
             c.execute(st)
             d=c.fetchall()
             for i in d:
                 print(i)
             m=input("Would you like to continue?y/n")
             if m in'Nn':
                 break    
                            
         print('************************************************************************************************************')
        
     #to find average age of student
            
    def avg_age():
         c.execute("select avg(age) from student")
         d=c.fetchall()
         for i in d:
             print(i)
             break
         print('************************************************************************************************************')
            
     #to arrange records as per roll number
     
    def arrange():
         c.execute("Select*from student order by roll")
         d=c.fetchall()
         for i in d:
             print(i)
         print('************************************************************************************************************')
       
     # to display name , city of those student whose fees are not paid
    def np():
         c.execute("Select name,city from student where fee=0")
         d=c.fetchall()
         print("These students have not paid the fees:")
         for i in d:
             print(i)

    print("Operations to be performed on student table:")
    print('1.Accept records')
    print('2.display records')
    print('3.search records')
    print('4.Update class of a student')
    print('5.delete a record')
    print('6.count distinct records')
    print('7.display distinct city')
    print('8.Displaying records by the char entered by the user')
    print('9.display average age of students')
    print('10.arranging records according to roll')
    print('11. to display name and phone number of students whose fees are not paid')      
            
    while True:
        ch=int(input("Enter choice(1-11):"))
        if ch==1:
            insert()
        elif ch==2:
            display()
        elif ch==3:
            search()
        elif ch==4:
            update_class()
        elif ch==5:
            delete()
        elif ch==6:
            count_dis()
        elif ch==7:
            distinct_display()
        elif ch==8:
            dis_char()
        elif ch==9:
            avg_age()
        elif ch==10:
            arrange()
        elif ch==11:
            np()
        else:
            print("Invalid choice")
        s=input("want to continue?y/n")
        if s in 'Nn':
            break
                   
v=input("Enter s to make changes in student table and t to make changes in teacher table:")

if v in'sS':
    student()
    
elif v in'tT':
    teacher()

con.close()


        
        
        
        
    
    



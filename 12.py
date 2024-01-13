#WAP to create a binary file to store Rollno,Name and Marks and update marks of entered Roll no
import pickle
def write():
    rec=[]
    while True:
        f=open('student.dat','wb')
        r=int(input("Enter roll :"))
        n=input("Enter name:")
        m=int(input("Enter marks:"))
        d=[r,n,m]
        rec.append(d)
        ch=input("Do you want to continue?Yy or Nn:")
        if ch in'nN':
            break
    pickle.dump(rec,f)
    f.close()
def update():
    f=open("Student.dat",'rb')
    roll=int(input("Enter roll number whose marks is to be updated"))
    m=int(input("Enter correct marks:"))
    z=pickle.load(f)
    for i in z:
        if i[0]==roll:
            i[2]=m
            print(i)
    f.close()
write()
update()
#Astha Kumari,12-E,roll-15

    
            

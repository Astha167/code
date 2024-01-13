#WAP to create CSV file and store empno, name, salary and search any empno and display name, salary and if not found appropriate message
import csv
'''def writer():
    f=open('employee.csv','w')
    w=csv.writer(f)
    data=['emp no','name','salary']
    w.writerow(data)
    while True:
        no=int(input("Employee no:"))
        name=input('Enter employee name')
        sal=int(input('Enter salary:'))
        w.writerow([no,name,sal])
        ch=input("Wanna append more data? y/n")
        if ch in'Nn':
            break
    f.close()    
def search():
    f=open('employee.csv','r')
    r=csv.reader(f)
    k=list(r)
    k.pop(0)
    for i in k:
        if i==[]:
            k.remove(i)       
    s=input('Enter the emp no whose data is to be searched:')
    c=0
    for j in k:
        if j[0]==s:
            name=j[1]
            salary=j[2]
            c=c+1
            print(name,salary)
            break
    if c==0:
        print("Record Not Found")
    f.close()          
writer()
search()
#Astha Kumari,12-E,roll=15
'''



'''def read():
    f=open("student.csv","r")
    x=csv.reader(f)
    for i in x:
        if i!=[]:
            print(i)
    f.close()'''

def COUNT():
    f=open("student.csv","r",newline='\n')
    x=csv.reader(f)
    next(f)
    
    c=0
    for i in x:
        if i!=[]:
            c=c+1
    print("Total no of rec",c)
    f.close()
#read()
COUNT()

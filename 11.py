#WAP to create a binary file with name and roll no.Search for a given roll number and display the name, if not found display appropriate message.
import pickle
def write():
    r=[]
    while True:
        f=open('record.dat','wb')
        roll=int(input('Enter roll number:'))
        name=input("Enter name:")
        d=[roll,name]
        r.append(d)
        ch=input("Do you want to enter more records yY/nN")
        if ch in'nN':
            break
    pickle.dump(r,f)
    f.close()
def search():
    f=open('record.dat','rb')
    r=int(input("Enter roll number to be searched"))
    c=0
    l=pickle.load(f)
    for i in l:
        if i[0]==r:
            print(i[1])
            c=c+1
            break
    if c==0:
        print("Record not found")
    f.close()
write()
search()
#Astha Kumari,12-E,roll-15

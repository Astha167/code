'''Raj has been asked to display all the students who have secured less than 40 for Remedial Classes.Write a user-defined function to display 
those students who have secured less than 40 from the binary file“Student.dat”.'''
import pickle
def read():
    f=open('student.dat','rb')
    x=pickle.load(f)
    for i in x:
        r=i[0]
        n=i[1]
        m=i[2]
        if m<40:
            print(r,n,m)
    f.close()
read()
#Astha Kumari,12-E,roll-15


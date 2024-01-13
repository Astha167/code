#WAP to read a text file line by line and display each word separated by #
f=open('display.txt')
x=f.readlines()
for i in x:
    k=i.split()
    for j in k:
        print(j,end='#')
#Astha Kumari,12-E,roll-15

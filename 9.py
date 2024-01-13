#WAP to remove all the lines that contain the character “b” in a file and write it into another text file
f=open('Education.txt')
x=f.readlines()
r=open('output.txt','w')
s=''
for i in x:
    for j in i:
        if j in'Bb' and i not in s:
           s=s+i
print(s)
r.write(s)
f.close()
r.close()
#Astha Kumari,12-E,roll-15

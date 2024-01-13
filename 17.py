#WAP to display the size of the file after removing EOL characters, leading and trailing white spaces and blank lines.
f=open("display.txt")
x=f.read()
c=0
for i in x:
    if i not in ',.;:-?'and i.isspace()==False:
        c=c+1
f.close()
print('Length of file after removing EOL and spaces:',c)
#Astha Kumari,12-E,roll-15

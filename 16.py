'''WAP to read a file ‘Story.txt’ and create an other file, storing an index of ‘Story.txt’, telling which line of the file each words appears in. If word appears more than once,then index should show
all the line numbers containing the word.'''
f=open('story.txt','r')
a=f.read()
fw=open('index.txt','w')
print(k)
d={}
file=' '
for i in k:
    r=i.strip('\r.?') 
    file=file+r+' '
g=file.lower()
s=file.split()
for j in s:
    c=0
    p=' '
    for y in s:
        if j==y:
           c=c+1
           p=p+str(c)+'  '
        d[j]=p
fw.write(str(d))
fw.close()
f.close()
#Astha Kumari,12-E, roll no-15
        

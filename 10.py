#WAP to read a text file and display the number of vowels/consonants/uppercase/lowercase characters in the file
f=open('display.txt')
x=f.read()
v=c=s=0
l=u=0
for i in x:
    if i in'AEIOUaeiou':
        v=v+1
    if i.islower():
        l=l+1
    if i.isupper():
        u=u+1
    if i not in'AEIOUaeiou.?!,:" " {)}[](/ 'and i.isspace()==False:
        c=c+1
print("Total no of vowels",v,"\nTotal no of consonants",c)
print("Total no of uppercase",u,"\nTotal no of lowercase",l)
#Astha Kumari,12-E,roll-15


#WAP to accept string/sentences from the user till the user enters “END”.Save the data in a text file and then display only those sentences which begin with an uppercase alphabet.
f=open('user.txt','w')
while True:
    s=input('Enter string/sentences:')
    f.write(s)
    f.write('\n')
    ch=input('Do you want to continue? type "END" to end the program else type "Y" to continue')
    if ch in 'ENDendEnd':
        break
f.close()
f=open('user.txt')
x=f.readlines()
for i in x:
    if i[0].isupper():
        print(i)
#Astha Kumari,12-E,roll-15   

#WAP to enter the string and display the longest word present in the entered string.
s=input('Enter a string:')
k=s.split()
h=' '
for i in k:
    if len(i)>len(h):
        h=i
print("longest word is:",h)
#Astha Kumari,12-E,roll-15
    

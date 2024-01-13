#WAP to check Armstrong No.
n=int(input("Enter a 3-digit number"))
d=s=0
p=n
print("Entered number is:",n)
while n!=0:
    d=n%10
    s=s+d**3
    n=n//10
if s==p:
    print(p,'is an armstrong no.')
else:
    print(p,'is not an armstrong no.')
#Astha Kumari,12-E,roll-15
    

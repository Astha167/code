#Write a program to enter the number of terms and to print the Fibonacci series
#Fibonacci series:0,1,1,2,3,5....
n=int(input('Enter number of terms:'))
a,b=0,1
print(a,b,end=' ')
for i in range(1,n-1):
    c=a+b
    print(c,end=' ')
    a=b
    b=c
#Astha Kumari,12-E,roll-15

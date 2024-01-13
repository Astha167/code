#WAF that takes a number as a parameter and checks whether a number is prime or not
def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c=c+1
    if c==2:
        print(a,'is prime')
    else:
        print(a,'is not prime')
a=int(input('Enter a number:'))
prime(a)
#Astha Kumari,12-E,roll-15




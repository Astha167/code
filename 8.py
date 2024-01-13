#Write a python function to calculate the factorial of a number (a non-negative integer).The function accepts the number whose factorial is to be calculated as the argument
import math as m
def factorial(n):
    k=int(m.fabs(n))
    p=1
    for i in range(1,n+1):
        p=p*i
    return("Factorial of",n,'is:',p)
n=int(input('Enter an integer'))
print(factorial(n))
#Astha Kumari,12-E,roll-15


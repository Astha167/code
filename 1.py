#Write a program to enter two numbers and print the arithmetic operations like +,-,*,/,//and% as per user choice.
def add(a,b):
    return(a+b)
def difference(a,b):
    return(a-b)
def product(a,b):
    return(a*b)
def division(a,b):
    return(a/b)
def floor_div(a,b):
    return(a//b)
def modulus(a,b):
    return(a%b)
x,y=eval(input('Enter a number:'))
print('1.Add \n2.Difference\n 3. Product \n4.Division\n 5. Floor division \n6.Modulus')
while True:
    ch=int(input('Enter your choice:'))
    if ch==1:
        print('Sum of',x,'and',y,'is:',add(x,y))
    elif ch==2:
        print('Difference of',x,'and',y,'is:',difference(x,y))
    elif ch==3:
        print('Product of',x,'and',y,'is:',product(x,y))
    elif ch==4:
        print('On dividing',x,'and',y,'we get:',division(x,y))
    elif ch==5:
        print('Floor division of',x,'and',y,'is:',floor_div(x,y))
    elif ch==6:
        print('Modulus of',x,'and',y,'is:',modulus(x,y))
    else:
        print('Invalid choice')
    i=input(('Do you want to continue? Enter Y or N'))
    if i in 'Yy':
        continue
    else:
        break
#Astha Kumari , 12-E,roll-15   
    
    
    

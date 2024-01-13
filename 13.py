#WAP to implement a stack using a list data structure
s=[]

#to push records in stack
while True:
    item=int(input("enter item:"))
    s.append(item)
    ch=input("Wanna append more?y/n")
    if ch in 'Nn':
        break

print('\n pushed elements in stack')    
#to display records
for i in range(len(s)-1,-1,-1):
    print(s[i])

#to display peek or topmist element
print('Topmost element is:',s[len(s)-1])

# to remove elements and empty stack
print('\n popped elements are:')
while True:
    if s==[]:
        print("\n Empty stack")
        break
    else:
        print(s.pop())
            
#Astha Kumari,12-E,roll-15

      

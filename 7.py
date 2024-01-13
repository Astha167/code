#WAP that accepts a hyphen-separated sequence of words as input and print the words in a hyphen-separated sequence after storing them alphabetically.
'''SampleItems:green-red-yellow-black-white
ExpectedResult:black-green-red-white-yellow'''
s=input('Enter a hypen-separated sequence :')
k=s.split('-')
k.sort()
r='-'.join(k)
print('Alphabetically arranged sequence is:',r)
#Astha Kumari,12-E,roll-15

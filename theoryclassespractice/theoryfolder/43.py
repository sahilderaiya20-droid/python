# how to create range i python 
'''
r1=range(10,200,2)
i=1
while i<=200: 
    print(i)
    i=i+1

for i in r1:
    print(i)


# write a first n natural numbers (USE range and for loop)
user=int(input("enter a n number"))
r1=range(1,user+1,1)
for i in r1:
    print(i)

# write a programm to print first n natural nnumbers squers
user=int(input("enter n munbers"))
r1=range(1,user+2)
for i in r1:
    print(i**2,end=" ")

# write a program to print first n even numbers 
user=int(input("enter n number as you wish"))
r1=range(1,user)
for i in r1:
    if i%2==0:
        print(i)
 
#   write a program to print first n even numbers in revers 

user=int(input("enter n number")) 
r1=range(user*2,1,-2)
for i in r1:
    print(i)
'''

# write a program to calculate sum of n numbers multiples of x
n=int(input("enter a n number"))
x=int(input("enter x value"))
s=0
for i in range(1,n+1):
    s=s+i*x
    print(s)
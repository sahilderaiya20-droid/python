#operators in python 

# 1st) arithmatic operator
# power(**)
'''
a=3**6
b=6**1000
c=3**2
print(a,b,c,end="--")
'''
'''
# division (/) it gives always float output 
a=4/2
print (a)   # output is 2.0

# floor division (//) it gives first value always
b=50//3
print(b) #output is 48 normal output is 
'''

'''
#modulo (%)
a=398%3
b=2%5
print(a,b)
'''
'''
# + (concatenation) and (addition)
a="abc"+"sahil"
print(a) 

b=5*"sahil"
print(b)
'''
'''
# relational operator (always gives true or false in the output)
a=10>20
b=30<50
c=10>=10
d=10=="10"
e=10!="10"
f="sahil"=="arman"
print(a,b,c,d,e,f,)
'''
'''
# logical operator (always write in lower case (and,or,not))

# and (when two conditions are true when and when it gives true atherwise it gives anser in false)
a=50<100 and 50>100
print(a) # false 

b=10==10 and 50<100
print(b) #true

# or (false or false = false ) (false or true = true) (true or false = true)

A=10<20 or 20>=50
print(A) #true
 
#  not (not true = false)  (not false = true)

B= not 20<30
print(B)

C=not True
print(C)
'''
"""
# bitwise operator (&,|,^,~,<<,>>)
a=13&52
print(a) #4

b=13|16
print(b) #29

c=13^36
print((c)) #41

d=~5
print(d) #-6

e=25>>3
print(e)

f=12<<3
print(f)
"""
'''
# assignment operator 
a=5
a+=10
print(a)

b=35
b*=35
print(b)

# assign multiple values to multiple variables in a single line 

a,b,c=10,20,30
print(a,b,c)
'''
'''
# identity operator (is ,is not)

a=20
b=20
print(id(a)) #id is 140718517606104
print(id(b)) #id is 140718517606104 
print(a is b)
print(a is not b)
'''
# membership operator (in,not in)

list=[1,2,3,4,5,6,7,]
print(5 in list)
print(9 not in list)
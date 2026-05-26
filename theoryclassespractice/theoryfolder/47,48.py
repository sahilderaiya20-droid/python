# str (string part-1)
'''
# how to create  string
s1="deraiya sahil"
s2='deraiya sahil'
s3="""deraiya sahil"""
s4=''deraiya sahil''
s5=str()
s6=str(123)
s7=str(3.45)
print(type(s1),s2,s3,s4,s5,s6,s7,end=" - ")

# how to accesing str elements 
S1="deraiya sahil"
print(S1[5])

# print full str
print(S1)

# using for loop 
for i in S1:
    print(i)

# slicing operator 
print(S1[0:4:1])

# built in functions 
print(len(S1))
print(max(S1))
print(min(S1))
print(sorted(S1))

# concatenation  and repetation  operator 

a1="sahil1"
a2="deraiya"
print(a1+a2)  #concatenation 
print(a1*2)   #repetation

# comparision operator 
print(a1>a2)

# str objects method 
print(a1.index("i"))
print(a1.count("i"))
print(a1.startswith("sa"))
print(a1.capitalize())
print(a1.islower())
print(a1.upper())

# formate 
s1="first={},secound={},third={}"
print(s1.format(2.5,4,"hello"))
S1=print("{},how are you ?".format("sahil"))

# split and join 
string="hello my name is deraiya sahil mahmadbhai"
s2=string.split(" ")
print(s2)   # output is =  ['hello', 'my', 'name', 'is', 'deraiya', 'sahil', 'mahmadbhai']

#  practice programm (taking list element from the user)
finallist = list(int(i) for i in input("Enter list elements: ").split("-"))
print(finallist)
'''
# join() function str
s1=["10","10","1983"]
print("-".join(s1))



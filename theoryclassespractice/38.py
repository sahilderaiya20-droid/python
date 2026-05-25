# decision controll
'''
# if condition

A=int(input("enter any  number: "))
B=int(input("enter another number: "))
if A>B:
    print("A is greater than B")
if A<B:
    print("B is greater than A")

# write a  program to check number is positive or nagative
A=int(input("enter a number: "))
if A>0:
    print("this number is positive")
if A<0:
    print("number is nagative")
'''
'''
# if else condition 
#  write a program to check a number is positive or nagatove using if else condition 
x=int(input("enter a number: "))
if x>=0:
    print("number is positive")
else:
    print("number is nagative")
'''
'''
# if elif else condition 
# write a prigram to print grade obtained in a test. taken obtained from user and display the grade 
GRADE=int(input("anter a marks"))
if GRADE>90 and GRADE<100:
    print("A grade")
elif GRADE>80 and GRADE<=90:
    print("B grade")
elif GRADE>70 and GRADE<=80:
    print("c grade")
elif GRADE>60 and GRADE<=70:
    print("d grade")
else:
    print("your child is only pass")

'''
'''
# single line if else codition
num=int(input("enter  number")) 
print ("positive") if num>=0 else print("nagative")
'''
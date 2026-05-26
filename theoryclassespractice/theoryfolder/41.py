#  transfer controll statment (syntax and small example)
#  break keyword
"""
i=1
while i<=10:
    print(i,end=" ")
    a=int(input(" enter a number"))
    if a<0:
        break
    i=i+1

# write a program to ask the user to enter a even number at most 4 times. if user failed to enter
# an all the three chances  than he lost the game, if user enter an even number , then no moer chances
# will be given and announce  him a winner 
i=1
while i<=4:
    player=int(input("enter a number "))
    if player%2==0:
        break
    i=i+1
if i==5:
    print("you are los the game")
else:
    print("you are win the game")

# continue (continue transfer the controll immideatly to the next iteration)
i=1
while i<=10:
    a=int(input("entyer a number "))
    if a%2==0:
        continue
    print(i,"a=",a)
    i=i+1
"""
# else eith while loop 
i=1
while i<=10:
    user=int(input("enter a number "))
    if user%2==0:
        print('you win the game')
        break
    i=i+1
else:
    print("you loss the game")

# pass


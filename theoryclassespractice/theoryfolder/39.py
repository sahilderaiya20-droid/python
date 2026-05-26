# match statment (like swith case)
'''
# match statment example
month=int(input("enter a any month number and gives a name of the month: "))
match month:
    case 1:
        print("january")
    case 2:
        print("february")
    case 3:
        print("march")
    case 4:
        print("april")
    case 5:
        print("may")
    case 6:
        print("jun")
    case 7:
        print("july")
    case 8:
        print("august")
    case 9:
        print("september")
    case 10:
        print("october")
    case 11:
        print("november")
    case 12:
        print("december")
    case _:
        print("default value")

'''
x=int(input("enter any number: "))
match x:
    case x if type(x)==int:
        print("this is the integer number")
    case x if type(x)==float:
        print("this is the float number")
    case x if type(x)==bool:
        print("this is the bool number")
    case _:
        print("default number")



"""
# for loop 
list=["sahil","aman","arman","rehan","azim","karis"]
count=0
for i in list:
    if i=="sahil":
        print("total number of a in list is =",i)
        count=count+1
        break
    else:
        print("no name in the list")
# for else

"""
# Take string input from user
text = input("Enter a string: ")

# Loop through each character
for ch in text:
    if ch == 'r':
        print("Character 'r' found. Stopping the loop.")
        break
    print(ch)

else:
    print("All characters are processed")

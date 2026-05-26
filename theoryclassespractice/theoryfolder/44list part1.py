# List (part 1)
"""
list1=[10,20,20,40] #simple list 
print(type(list1)) #type of the list 
print(list1)  #print the list


list2=[]  #empty list
print(type(list2))
print(list2)

l3=["sahil",20,5.3] # hetrogeneus list 
print(l3[2],l3[0]) #also print perticular elements 

# nagative indexing 
l1=[10,70,80,56,89,74,90]
print(l1[-1],l1[-3],l1[2])

# access list elemrnts using for loop and while loop 

# for loop 
l1=[10,20,30,40,50,60]
for i in l1:
    print(i,end=" ")

# while loop
l1=[10,20,30,40,50,60,70]
i=0
while i<=5:
    print(l1[i],end=" ")
    i=i+1

# delete element from the list 
l1=[10,20,30,40,50]
del l1[2]
print(l1)

l2=[10,20,30,40,50]
l2 [3]=100
print(l2)
"""
# how to add more elements in the list
# 1) using append you are add element in the end of the list
l1=[10,20,30,40,50,60,70]
l1.append(100)
print(l1)

# 2) using insert 
l2=[10,20,30,40,50,60,70]
l2.insert(1,100)
print(l2)



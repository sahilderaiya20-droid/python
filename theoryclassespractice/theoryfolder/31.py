#print methods (there are four methods)
'''
1)print()
2)sep
3)end
4)special characters
'''

''' this  is the print method
print("sahil") # output is sahil
print(1+2+3)  #output is 6
print(1*2*3)  #output is 6 
print(1+2,2-1,"sahil") #output is 3 1 sahil
a=5
print(a) 

'''
''' using sep=""
a=1
b=2
c=3
print(a,b,c)  #output is 1 2 3 
print(a,b,c,sep="..") #output is 1..2..3
print(a,b,c,sep="--") #output is 1--2--3

'''
'''

#use of end=""
print("sahil",end=",,,")
print(1+2+3*4) # output is sahil,,,15

'''
#(mix of end sep)
a=1
b=2
c=3
print(a,b,c,sep="--",end=",,,")
print("sahil") #output is 1--2--3,,,sahil
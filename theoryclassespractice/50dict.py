# dictionary
sahil={0:"roll number ",1:"name",2:"email",3:"cource"}
m=dict(rollnumber=103,cource="btechcse",)
print(sahil,m)
print(type(m))
for i in sahil:
    print(i)

for j in sahil:
    print(j,sahil[j])

# update element 

sahil[1]="arman"
print(sahil)

# delete element 

sahil[1]
sahil[1]="yyyyy"
print(sahil)

# methods 
print(sahil.items())
print(sahil.keys())
print(sahil.values())

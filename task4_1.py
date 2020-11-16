string="three four five six"
d=string.split()
print(d)
list=[3,4,5,6]
dict1=dict(zip(d,list))
print(dict1)
sum=0
for i in dict1:
    b=dict1[i]
    sum=sum+b
print(sum)

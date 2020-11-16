list=[10,20,20,10,10,30,50,10,20]
i=0
while(i<len(list)):
    j=0
    count=0
    while(j<len(list)):
        if list[i]==list[j]:
            count=count+1
        j=j+1
    i=i+1
print(count)

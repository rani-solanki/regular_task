# price=int(input("enter the number"))
# start=int(input("enter the number"))
# for i in range(start,price+1):
#     if (i%3==0 or i%5==0):
#         print(i)

# year=int(input("enter the number"))
# if year%4==0 and year%100!=0:
#     print("leap yaer",year)
# elif year%400==0:
#     print("leap year",year)
# else:
#     print("it is not leap year",year)


# user=int(input("enter the number"))
# even_list=[]
# odd_list=[]
# for i in range(1,user):
#     if i%2==0:
#         even_list.append(i)
# for j in range(1,user+6):
#     if j%2!=0:
#         odd_list.append(j)
# num=4
# for x in range(1,num):
#     print('even number',even_list[-x])
# for y in range(1,num):
#     print( 'odd number',odd_list[-y])



# year=int(input("enter the number"))
# year2=year-6
# year1=year+6
# print(year1)
# print(year2)
# for i in range(year2,year1):
#     print(i)
#     if year1%4==0 and year1%100!=0:
#         print("leap yaer",year1)
#     elif year1%400==0:
#         print("leap year",year1)
#     else:
#         print("it is not leap year",year1)

# amstrong number
# user=input("enter the number")
# j=int(user)
# b=0
# for i in user:
#     b=b+int(i)**3
# print(b)
# if b==j:
#     print("it is armstrong number")
# else:
#     print("it is not armstrong number")

# user=int(input("enter the number"))
# i=0
# while(i<user):
#     j=0
#     m=0
#     while(j<=i):
#         m=m+int(j)**3
#         j=j+1  
#     if m==i:
#         print("yes",i)
#     i=i+1

# we have to find armstrong number between 1 to 1000.
# user=int(input("enter the number"))
# i=1
# while(i<user):
#     j=0
#     m=0
#     h=str(i)
#     while(j<len(h)):
#         k=(h[j])
#         m=m+int(k)**3
#         j=j+1
#     # print(m)
#     if m==i:
#         print("yes",i)
#     i=i+1
#  how to find perfect number

# user=int(input("enter the number"))
# i=10
# while(i<user):
#     j=0
#     m=0
#     d=str(i)
#     while(j<len(d)):
#         f=d[j]
#         m=m+int(f)
#         j=j+1
#     if m==i:
#         print("yes",i)
#     i=i+1
# user=int(input("enter the number"))
# j=1
# while(j<user):
#     i=1
#     k=0
#     while(i<j):
#         if (j%i==0):
#             k=k+i   
#         i=i+1
#     if(k==j):
#         print("yes",j)
#     j=j+1

# def solveMeFirst(a,b):
#     h=a+b
#     return(h)

# def solveMeFirst(x,y):
#     return x+y

# num1 = int(input("enter the number"))
# num2 = int(input("enter the number"))
# res=solveMeFirst(num1,num2)
# print(res)

# hakaren qusetion
i=2
j=5
h=(2+5)/2
print(h)

list=[1,3,3,7,5,2,7]
list1=[]
for i in range(len(list)):
    count=0
    for j in list:
        if j in list1:
            list1.append(j)
            count=count+1
    print(count,list[i])
print(list1)
    
    
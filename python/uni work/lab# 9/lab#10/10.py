# program1

# def ball(i):
#     a=()
#     x=int(input("Enter value of x{}     ".format(i)))
#     y=int(input("Enter value of y{}     ".format(i)))
#     r=int(input("Enter value of r{}     ".format(i)))
#     a=list(a)
#     a.insert(0,x)
#     a.insert(1,y)
#     a.insert(2,r)
#     a=tuple(a)
#     return(a)
# import math
# x="1"
# y="2"
# b1=ball(x)
# b2=ball(y)
# print(b2)
# print(b1)
# distance=math.sqrt((b2[0]-b1[0])**2 + (b2[1]-b1[1])**2)
# radius_some=b1[2]+b2[2]
# if distance<=radius_some:
#     print("Weather the given two balls colliding ? True")
# else:
#     print("Weather the given two balls colliding ? False")
    
# program2

# def data():
#     l=[]
#     x=int(input("Enter the size of list "))
#     for i in range(x):
#         a=int(input("Enter an element   "))
#         l.append(a)
#     return(l)
# Sum=0
# marks=data()
# length=len(marks)
# for i in range(length):
#     Sum=Sum+marks[i]
# mean=Sum/length
# marks.sort()
# marks1=marks
# print(marks1)
# print(length)
# if length%2!=0:
#     middle=int((length-1)/2)
#     median=marks1[middle]
# else:
#     x=int(length/2)
#     y=x-1
#     middle1=marks1[x]
#     middle2=marks[y]
#     median=(middle1+middle2)/2
    
# dict_mode={}
# mode=[]
# for i in range(length):
#     if  marks[i] in dict_mode.keys():
#        dict_mode[marks1[i]]+=1
#     else:
#         dict_mode[marks1[i]]=1
# print(dict_mode)   #test
# max_frequency_list=[]
# for i in dict_mode.values():
#     max_frequency_list.append(i)
# max_frequency_list.sort()
# max_frequency=max_frequency_list[-1]
# print(max_frequency) # test
# length1=len(dict_mode)
# for i in dict_mode.values():
#     if i==max_frequency:
#         a=list(dict_mode.keys())
#         b=list(dict_mode.values())
#         f=a[b.index(i)]
#         mode.append(f)
#         break
# print("Mean =   {}".format(mean))
# print("Median =   {}".format(median))
# print("Mode =   {}".format(mode))

# #program 3

# s1=str(input('enter string1=    '))
# s2=str(input('enter string2=    '))
# m=len(s1)
# n=len(s2)
# if abs(m-n)>1:
#     print("Two String are not nearly equal")

# j=0
# count=0
# i=0
# while i<m and j<n:
#     if s1[i]==s2[j]:
#         i+=1
#         j+=1
#     elif m>n:
#         i+=1
#         count+=1
#     elif m<n:
#         j+=1
#         count+=1
#     else:
#         i+=1
#         j+=1
#         count+=1
# if count==1:
#     print("Two String are nearly equal")
# else:
#     print("Two String are not nearly equal")

#program 4


# def data():
#     l=[]
#     x=int(input("Enter the size of list "))
#     for i in range(x):
#         a=int(input("Enter an element   "))
#         l.append(a)
#     return(l)
# dict_dups={}
# list_dict=[]
# list1=data()
# for i in list1:
#     if i in dict_dups.keys():
#         dict_dups[i]+=1
#     else:
#         dict_dups[i]=1
# length=len(dict_dups)
# count=0
# for i in dict_dups.values():
#     if i>1:
#         k=list(dict_dups.keys())
#         v=list(dict_dups.values())
#         list_dict.append(k[count])

#     count+=1
# print("The duplicate elements in the list are:")    
# print(list_dict)

# program5


# def data():
#     l=[]
#     x=int(input("Enter the size of list "))
#     for i in range(x):
#         a=int(input("Enter an element   "))
#         l.append(a)
#     return(l)
# dict_dups={}
# list_dict=[]
# list1=data()
# for i in list1:
#     if i in dict_dups.keys():
#         dict_dups[i]+=1
#     else:
#         dict_dups[i]=1
# length=len(dict_dups)
# count=0
# for i in dict_dups.values():
#     if i>1:
#         pass
#     else:
#         k=list(dict_dups.keys())
#         v=list(dict_dups.values())
#         list_dict.append(k[count])
#     count+=1
# print("The unique elements in the list are:")
# print(list_dict)


# program6
# def data():
#     l=[]
#     x=int(input("Enter the size of list "))
#     for i in range(x):
#         a=int(input("Enter an element   "))
#         l.append(a)
#     return(l)
# cum_product_list=[]
# prod=1
# l=data()
# for i in l:
#     prod=prod*i
#     cum_product_list.append(prod)
# for i in cum_product_list:
#     print(i)


# # program7
# def data():
#     l=[]
#     x=int(input("Enter the size of list "))
#     for i in range(x):
#         a=int(input("Enter an element   "))
#         l.append(a)
#     return(l)
# l=data()
# print("orignal list is ")
# print(l)
# r=-1
# rev=[]
# for i in l:
#     rev.append(l[r])
#     r-=1
# print("reversed list  is ")
# print(rev)

# program8

# def gdc(a,b):
#     if b==0:
#         return a
#     else:
#         x=b
#         b=a%b
#         x=gdc(x,b)
#         return(x)
# def lcm(a,b):
#     x=(a*b)/gdc(a,b)
#     return(x)
# a=int(input("Enter First Number:     "))
# b=int(input("Enter Second Number:    "))
# x1=gdc(a,b)
# x2=lcm(a,b)
# print("LCM of two numbers is :  {}".format(x2))
# print("GDC of two numbers is :  {}".format(x1))

# a=10
# b=20
# def change():
#     global b
#     a=45
#     b=56
# change()
# print(a)
# print(b)

# def change(one, *two):
#     print(type(two))
# change(1,2,3,4)

# import sys
# print(type(sys.argv))

# x = 5
# def f1():
# 	global x
# 	x = 4
# def f2(a,b):
# 	global x
# 	return a+b+x
# f1()
# total =f2(1,2)
# print(total)

# x=100
# def f1():
# 	global x
# 	x=90
# def f2():
#     global x
# x=80
# print(x)



# def f(m,n):
#     ans = 1
#     while (m - n >= 0):
#         (ans,m)=(ans*2,m-n)
#     return(ans)
# x=f(120,13)
# print(x)

# def g(x,y):
#     val = 0
#     while (x > y):
#         (val,x) =(val+1,x/y)
#     return(val)
# print(g(9000,3))

# y,z=1,2
# def f():
#     global x
#     x=y+z
#     return (z)
# a=f()
# print(a)\

x=1

while x<5:
    if x==2:
        print(x)
        continue
        print("ihg")    
    x+=1
    print(x)
# you have to calculate first four central moments about mean(journal aur excel sheet mai solve krna hai ) Ungroup data

# you have to calculate first four central moments about mean(journal aur excel sheet mai solve krna hai )group data

# you have to calculate first four central moments about zero (journal aur excel sheet mai solve krna hai )group data

# no mcqs only theory + problems (Stats)
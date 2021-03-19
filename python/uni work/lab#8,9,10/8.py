# fib1=1
# fib2=2
# fib3=fib1+fib2
# Sum=0
# while fib3<4000000:
#     if fib3%2==0:
#         Sum=Sum+fib3
#     fib1=fib2
#     fib2=fib3
#     fib3=fib1+fib2
# print("the sum of even fibocani numbers below 4 million is  {}".format(Sum+2))
# for i in range(100,30,-20):
#     print(i)
# x=str(input("enter string!   "))
# e=str(input("enter string you wnt to count in word !   "))
# y={}
# z=0
# for i in x:
#     y[z]=x[z]
#     z=z+1
# c=0
# for i in x:
#     if i==e:
#         c=c+1

# print("The count of word {} in {} is {}".format(e,x,c))

# birthday={"SANA":"15/07/1989", "ASAD":"09/12/1988","RAZA":"11/02/2016"}
# x=input("Enter date of birth in format (dd-mm-yyyy)     ")
# date_list=x.split("-")
# dob="/".join(date_list)
# for key,value in birthday.items():
#     if dob==value:
#         print("Date of birth found in the dictionary whose name is {} ".format(key))
#         break
# else:
#     print("Date of birth not found")

def list(word):
    l=[]
    n=int(input("Enter length of the list   "))
    for i in range(n):
        x=input("Enter  {} ".format(word))
        l.append(x)
    return(l)
names=list("names")
salaries=list("salaries")
person_dist={}
j=0
print(names)
print(salaries)
for i in names:
    person_dist[names[j]]=salaries[j]
    j=j+1
print(person_dist)
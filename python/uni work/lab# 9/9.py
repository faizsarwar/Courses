#aim1


# file_name=str(input("Enter fiel name !   "))
# file_contents=open(file_name,'r')
# dict={}
# for z in file_contents:
#     for x in z:
#         if x in dict.keys():
#             dict[x]+=1
#         else:
#             dict[x]=1
# print(dict)
# print(len(dict))

# if file_name.endswith(".c"):
#     print("Input file is C program file")
# if file_name.endswith(".py"):
#     print("Input file is python program file")
# if file_name.endswith(".txt"):
#     print("Input file is text file")



# program # 2


# file_name=str(input("Enter fiel name !   "))
# file_contents=open(file_name,'r')
# for i in file_contents:
#     file_content=i.split()
# for i in file_content:
#     a=i[::-1]
#     print(a)
# file_contents.close()
        
# program # 3


# file_name=str(input("Enter fiel name !   "))
# file_contents=open(file_name,'r')
# noc=0
# nol=1
# now=1
# for i in file_contents:
#     for z in i:
#         noc+=1
#         if z=="\n":
#             nol+=1
#         if z==" " and "\n":
#             now+=1
# print("Number of lines :  {}".format(nol))
# print("Number of characters :  {}".format(noc))
# print("Number of word :  {}".format(now))



def compare(list1,list2):
    set(list1)
    set(list2)
    if list1==list2:
        print("lists are equal ! ")
    else:
        print("list are not equal ! ")
li=[1,3,4]
lii=[2,3,5]
print(compare(li,lii))
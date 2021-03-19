
# #######################  Example # 1  (Opertaor overloading)

# class student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#     def __add__(self,other):    # add ka function apnay hisab say set krsktay hain wrna predefined function use huga
#         m1=self.m1+other.m1
#         m2=self.m2+other.m2
#         s3 = student(m1,m2)
#         return s3


# s1=student(56,"ss")

# s2=student(33,"ss")

# s3=s1+s2   # add ka function class student keliye define nhi hai hm define krengay exisisting function change bhi krsktay hain

# print(s3.m2)

######################  Example # 2 (method overloading)

# class student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2

#     def __add__(self,a=None,b=None,c=None):    # add ka function apnay hisab say set krsktay hain wrna predefined function use huga (Overlaoding)
#         s=0
#         if c==None:
#             s=a+b
#         elif b==None and c==None:
#             s=a
#         else:
#             s=a+b+c                                # agr teen parameters pass nhi hungay tu error ajaiga kiunkay none type int mai add nhi huti islye if condition lagaingay error handling keliye
#         return s
# s=student(2,3)
# print(s.__add__(3,3))

####################  Example # 3 (method over riding)
# class A:
#     def show(self):
#         print("In a show")
# class B(A):
#     def show(self):                     # agr b mai show fn hug a tu b mai dekhega wrna a mai
#         print("In  b show")
# s1=B()
# s1.show()

################## Example # 4 (abstract_methods and abstract_classes)
# from abc import ABC,abstractmethod

# class computer(ABC):     # ABC stands for (abstract base class) 
#     @abstractmethod         
#     def process(self):
#         pass
# class laptop(computer):
#     pass

# com=computer()        # abstract method ka object nhi bana sktay hm
# s1=laptop()            # is class ka bhi instance nhi ban skta ku=iunkay ye bhi computer say assosiate hai
# com.process()

################## Example # 5 (iterator)
# nums=[2,3,4,5,6]
# it = iter(nums)                 # iter ka function hai usmai next ka method hai hamain aik value deta hai dobara iteration pr us say next value deta hai
# print(it.__next__())
# print(it.__next__())            
                            # making our own iterator
class topten:
    def __init__(self):
        self.num=1
    def __iter__(self):         # pre defined function ko change krnay keliye whi name use krna huga (_ _) laga kay
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration                     # error handler hai iteration stop krta hai
values=topten()
for i in values:
    print(i)
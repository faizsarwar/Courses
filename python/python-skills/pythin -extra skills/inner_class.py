#######################--Example-1

# class student:
#     def __init__(self,name,age):                    # init ka function execute zaror hua agr call nhi krengay jb bhi nhi define krengay jb bhi huga internally agr define krengay tu ju define kia hai wo call huga
#         self.name=name                              # also called constructor
#         self.age=age
#         self.lap=self.laptop()

#     def show(self):
#         print(self.name,self.age)
#         self.lap.show()

#     class laptop:
#         def __init__(self):
#             self.brand="HP"
#             self.cpu="i5"
#             self.ram="8gb"
#         def show(self):
#             print(self.brand,self.cpu,self.ram)


# s1=student("faiz",20)
# s2=student("Ali",21)
# lap1=s1.lap
# lap2=s2.lap

# s1.show()
# s2.show()

#####################------------Example-2

# class A:
#     def feature1(self):
#         print("feature 1 is working")
#     def feature2(self):
#         print("feature 2 is working")
# class B:
#     def feature3(self):
#         print("feature 3 is working")
#     def feature4(self):
#         print("feature 4 is working")
# class C(A,B):                                   # class inheritance of muiltiple class can access both class 
#     def feature5(self):
#         print("feature 5 is working")

# c1=C()
# c1.feature4()

###############################----------------EXample # 3

# class A:
#     def __init__(self):
#         print("inside A init")

#     def feature1(self):
#         print("feature 1 is working")
#     def feature2(self):
#         print("feature 2 is working")
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("inside B init")
#     def feature3(self):
#         print("feature 3 is working")
#     def feature4(self):
#         print("feature 4 is working")
#         # b ki class say object banaingay tu init k function call huga agr B mai init define nhi tu A ka call krega wrna A ka krega 
#         # agr humaain dono init function krnay hain tu super ka keyword use huga 
# b1=B()

########################------------------Example # 4
# class A:
#     def __init__(self):
#         print("in A init")

#     def feature1(self):
#         print("feature 1 is working")
#     def feature2(self):
#         print("feature 2 is working")
# class B:
#     def __init__(self):
#         print("in B init")
#     def feature3(self):
#         print("feature 3 is working")
#     def feature4(self):
#         print("feature 4 is working")
# class C(A,B):  
#     def __init(self):
#         super().__init()                                   #super with init sirf init k function mai hi call huga                         
#         print("in c init")                                #super ka function dono parent class mai sai left walay execute kega 
#     def feature5(self):
#         print("feature 5 is working")

# c1=C()
# c1.feature4()

############################---Example # 5

# class laptop:
#     def code(self,ide):
#         ide.execute(self)              ##(duck typing) laptop wala execute ka function dono classes say execute huskta hai bs un clases mai execute ka function huna chaiye
# class vs_code:
#     def execute(self):
#         print("compiling")
#         print("executing")
# class pycharm:
#     def execute(self):
#         print("spell checker")
#         print("error detector")

# a=pycharm()
# len(a)
# b=vs_code()
# faiz=laptop()
# faiz.code(vs_code)
# faiz.code(pycharm)

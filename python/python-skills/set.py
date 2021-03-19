# A set is a mutable list but it does not allow duplicate like array does an empty sdet is considered as a dictionary 

myset={}
print(type(myset))   # shows type as a dictionary 
myset=set({})
print(type(myset))   # shows type as a set
myset={1,2,2,3,3,9}
print
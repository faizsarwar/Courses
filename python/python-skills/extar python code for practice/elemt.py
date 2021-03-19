a=[2,3,4,5,6]
b=[0,1,2,3,4]
c=[10,0,9,8,7,6,5]
f=[]
f.append(a)
f.append(b)
f.append(c)
el=int(input("Enter a number to myultiply        "))
r=int(input("Enter the number of row to be multiply with!!      "))
row=f[r-1]
result=[]
for i in row:
    s=i*el
    result.append(s)
f.insert(r-1,result)
f.pop(2)
for i in f:
    print(i)
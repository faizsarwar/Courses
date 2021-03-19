ncA=int(input("enter the number of coloumbs A"))
nrA=int(input("enter the number of Rows A"))




A=[]
for r in range(nrA):
    R=[]
    for c in range (ncA):
        a=float(input("enter the value for Matrix A: "))
        R.append(a)
    A.append(R)
B=[]
for r in range(nrA):
    R=[]
    for c in range (ncA):
        a=float(input("enter the value for Matrix b: "))
        R.append(a)
    B.append(R)
C=[]
for r in range(nrA):
    R=[]
    for c in range(ncA):
        a=A[r][c]+B[r][c]
        R.append(a)
    C.append(R)
print(A)
print(B)
print(C)
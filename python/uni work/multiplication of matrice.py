

x=int(input("Enter length of first square matrix  A     "))
first=[]
def matrixInput(numberOfRows, numberOfColumns, message=": "):
    M=[]
    for r in range(numberOfRows):
        R=[]
        for c in range(numberOfColumns):
            a=float(input("Enter a value for matrix "+message))
            R.append(a)
    
        M.append(R)
    return(M)


y=int(input("Enter length of second square matrix B     "))
second=[]

def output(matrix,lengthR,lengthC):
    for w in range(lengthR):
        for i in range(lengthC):
            print(matrix[w][i], end="    ")
        print("\n")


a=matrixInput(x,x)
print("Matrix A is :")
output(a,x,x)

b=matrixInput(y,y)
print("Matrix b is :")
output(b,y,y)

def matrix_multiplication(A,B,lengthA,lengthB,lengthbc):
    result=[]
    for i in range(lengthA):
        c=[]
        for z in range(lengthB):
            c.append(0)
        result.append(c)

# iterate through rows of X
    for i in range(lengthA):
   # iterate through columns of Y
        for j in range(lengthbc):
       # iterate through rows of Y
            for k in range(lengthB):
                result[i][j] += A[i][k] * B[k][j]

    return(result)
bc=len(b[0])
x1=matrix_multiplication(a,b,x,y,bc)
lr=len(x1)
lc=len(x1[0])
print("multiplicative matrice is")
output(x1,lr,lc)


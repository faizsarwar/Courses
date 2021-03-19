"""
def matrixAInput():
    r = 0
    while (r < nrA):
        R=[]
        c = 0
        while(c < ncA):
            a=float(input("Enter a value for matrix :"))
            R.append(a)
            c += 1 
        A.append(R)
        r += 1

def matrixBInput():
    r = 0
    while (r < nrB):
        R=[]
        c = 0
        while(c < ncB):
            a=float(input("Enter a value for matrix :"))
            R.append(a)
            c += 1 
        B.append(R)
        r += 1
"""
def matrixInput(numberOfRows, numberOfColumns, message=": "):
    M=[]
    for r in range(numberOfRows):
        R=[]
        for c in range(numberOfColumns):
            a=float(input("Enter a value for matrix "+message))
            R.append(a)
    
        M.append(R)
    print(M)
    return(M)


def rows_interchange(matrix,first_row,Second_row):
    y=matrix[first_row]
    z=matrix[Second_row]
    matrix.insert(first_row,z)
    matrix.remove(matrix[first_row+1])
    matrix.insert(Second_row,y)
    matrix.pop(Second_row+1)
    return(matrix)

def matrix_square(matrix):
    A=matrix
    B=matrix
    nrA=len(matrix)
    x=matrix[0]
    ncB=len(x)
    C=[]
    r = 0
    while (r < nrA):
        R=[]
        c = 0
        while(c < ncB):

            k=0
            s = 0
            while ( k < ncA):
                a=A[r][k] * B[k][c]                  
                s += a
                k += 1

            R.append(s)
            c += 1 

        C.append(R)
        r += 1
    return(C)

def matrix_cube(matrix_square,matrix):
    A=matrix_square
    B=matrix
    x=B[0]
    nrA=len(A)
    ncB=len(x)    
    C=[]
    r = 0
    while (r < nrA):
        R=[]
        c = 0
        while(c < ncB):

            k=0
            s = 0
            while ( k < ncA):
                a=A[r][k] * B[k][c]                  
                s += a
                k += 1

            R.append(s)
            c += 1 

        C.append(R)
        r += 1
    return(C)


#---------------------


ncA = int(input("enter number of coloumns of matrix A: "))
nrA = int(input("enter number of rows of matrix A: "))

ncB = int(input("enter number of coloumns of matrix B: "))
nrB = int(input("enter number of rows of matrix B: "))

if (ncA != nrB):
    print ("Can't multiply")
else:
    
    A=matrixInput(numberOfColumns=ncA,numberOfRows=nrA,message=" A:")

    B=matrixInput(numberOfColumns=ncA,numberOfRows=nrB,message=" B:") 
    
    sq=matrix_square(B)
    print("square of matrix B is ",sq)

    cube=matrix_cube(sq,B)
    print("cube of Matrix B is",cube)
    
    ch=matrixInput(numberOfColumns=ncA,numberOfRows=nrA,message=" c:") 

    u=rows_interchange(ch,0,1)
    print("interchanged matrix is",u)

    C=[]
    r = 0
    while (r < nrA):
        R=[]
        c = 0
        while(c < ncB):

            k=0
            s = 0
            while ( k < ncA):
                a=A[r][k] * B[k][c]                  
                s += a
                k += 1

            R.append(s)
            c += 1 

        C.append(R)
        r += 1
        
print("matrix 'A' multiply by matrix  'B' is ",C)

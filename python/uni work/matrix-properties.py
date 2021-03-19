def matrixInput(numberOfRows, numberOfColumns, message=": "):
    M=[]
    for r in range(numberOfRows):
        R=[]
        for c in range(numberOfColumns):
            a=float(input("Enter a value for matrix "+message))
            R.append(a)
    
        M.append(R)
    return(M)

def output(matrix,numberOfrows,numberOfColumns,message=": "):
    print("Matrix {} is !!!".format(message))
    print('\n')
    for w in range(numberOfrows):
        for i in range(numberOfColumns):
            print(matrix[w][i], end="    ")
        print("\n")
    
nrA=int(input("Enter the number of rows of first matrix   "))
ncA=int(input("Enter the number of coloumns of first matrix  "))
nrB=int(input("Enter the number of rows of Second matrix   "))
ncB=int(input("Enter the number of coloumns of Sceond matrix  "))

a=matrixInput(numberOfRows=nrA,numberOfColumns=ncA,message=' A    ')
b=matrixInput(nrB,ncB,message='B    ')

output(a,nrA,ncA,message=": A")
output(b,nrB,ncB,message=": B")

def check_square(numberOfRows,numberOfColumns,message=': '):
    if numberOfRows==numberOfColumns:
        print("{} is a square matrix ".format(message))
    else:
        print("{} is not a square matrix ".format(message))

def check_equality(matrixA,matrizB,numberOfRowsA,numberOfColumnsA,numberOfRowsB,numberOfColumnsB):
    if numberOfRowsA==numberOfRowsB and numberOfColumnsA==numberOfColumnsB:
        c=0
        for i in range(numberOfRowsA):
            for j in range(numberOfColumnsA):
                if matrixA[i][j]==matrizB[i][j]:
                    c=0
                else:
                    c=1
                c=0+c
        if c==0:
            print("Matrices are equal !!")
        else:
            print("Matrices are not equal !!")            
    else:
        print("matrices are not equal !!")

def check_null(matrixA,matrixB,numberOfRowsA,numberOfColumnsA,numberOfRowsB,numberOfColumnsB):
    a=[matrixA,matrixB]
    message=['A','B']
    b=len(a)
    s=[[numberOfRowsA,numberOfColumnsA],[numberOfRowsB,numberOfColumnsB]]
    for k in range(b):
        c=0
        for i in range(s[k][0]):
            for j in range(s[k][1]):
                if a[k][i][j]!=0.0:
                    c=1
        if c==1:
            print("Matrix {} is not a null Matrix !!".format(message[k]))           
        else:
            print("Matrix {} is a null Matrix !!".format(message[k]))   

def check_scalar(matrixA,matrixB,numberOfRowsA,numberOfColumnsA,numberOfRowsB,numberOfColumnsB):
    a=[matrixA,matrixB]
    message=['A','B']
    b=len(a)
    s=[[numberOfRowsA,numberOfColumnsA],[numberOfRowsB,numberOfColumnsB]]
    for k in range(b):
        c=[]
        for i in range(s[k][0]):
            for j in range(s[k][1]):
                if s[k][0]==s[k][1]:
                    if i==j:
                        if a[k][i][j]!=0:
                            c.append(0)
                    else:
                        if a[k][i][j]==0:
                            c.append(0)
                        else:
                            c.append(1)
                       
                else:
                    c.append(1)
        x=len(c)
        y=0
        for i in range(x):
            if c[i]==y:
                z=0
            else:
                z=1
                print("Matrix {} is not a singular Matrix !!".format(message[k]))
                break
        if z==0:
            print("Matrix {} is a singular Matrix !!".format(message[k]))     

def check_unit(matrixA,matrixB,numberOfRowsA,numberOfColumnsA,numberOfRowsB,numberOfColumnsB):
    a=[matrixA,matrixB]
    message=['A','B']
    b=len(a)
    s=[[numberOfRowsA,numberOfColumnsA],[numberOfRowsB,numberOfColumnsB]]
    for k in range(b):
        c=[]
        for i in range(s[k][0]):
            for j in range(s[k][1]):
                if s[k][0]==s[k][1]:
                    if i==j:
                        if a[k][i][j]==1:
                            c.append(0)
                        else:
                            c.append(1)
                    else:
                        if a[k][i][j]==0:
                            c.append(0)
                        else:
                            c.append(1)
                else:
                    c.append(1)
        x=len(c)
        y=0
        for i in range(x):
            if c[i]==y:
                z=0
            else:
                z=1
                print("Matrix {} is not a unit Matrix !!".format(message[k])) 
                break                                      
        if z==0:
            print("Matrix {} is a unit Matrix !!".format(message[k]))    

def check_diagonal(matrixA,matrixB,numberOfRowsA,numberOfColumnsA,numberOfRowsB,numberOfColumnsB):
    a=[matrixA,matrixB]
    message=['A','B']
    b=len(a)
    s=[[numberOfRowsA,numberOfColumnsA],[numberOfRowsB,numberOfColumnsB]]
    for k in range(b):
        if s[k][0]==s[k][1]:
            c=[]
            for i in range(s[k][0]):
                for j in range(s[k][1]):
                        if i==j:
                            if a[k][i][j]!=0.0:
                                c.append(1)
                        else:
                            if a[k][i][j]==0.0:
                                c.append(1)                    
                            else:
                                c.append(0)        
            x=len(c)
            y=1
            for z in range(x):
                if c[z]==1:
                    w=0
                else:
                    w=1
                    print("Matrix {} is not a  daigonal Matrix !!".format(message[k]))  
                    break
            if w==0:
                print("Matrix {} is a  daigonal Matrix !!".format(message[k]))  
        else:
            print("Matrix {} is not a  daigonal Matrix !!".format(message[k]))           
            
def check_symmetric(numberOfRowsA,numberOfColumnsA,numberOfRowsB,numberOfColumnsB):
    if numberOfRowsA==numberOfRowsB and numberOfColumnsA==numberOfColumnsB:
        print("Matrix A and B are symmetric")
    else:
        print("Matrix A and B are not symmetric")

def check_identity(matrixA,matrixB,numberOfRowsA,numberOfColumnsA,numberOfRowsB,numberOfColumnsB):
    a=[matrixA,matrixB]
    message=['A','B']
    b=len(a)
    s=[[numberOfRowsA,numberOfColumnsA],[numberOfRowsB,numberOfColumnsB]]
    for k in range(b):
        c=[]
        for i in range(s[k][0]):
            for j in range(s[k][1]):
                if s[k][0]==s[k][1]:
                    if i==j:
                        if a[k][i][j]==1:
                            c.append(0)
                        else:
                            c.append(1)
                    else:
                        if a[k][i][j]==0:
                            c.append(0)
                        else:
                            c.append(1)
                else:
                    c.append(1)
        x=len(c)
        y=0
        for i in range(x):
            if c[i]==y:
                z=0
            else:
                z=1
                print("Matrix {} is not a unit Matrix !!".format(message[k])) 
                break                                      
        if z==0:
            print("Matrix {} is a unit Matrix !!".format(message[k]))    

def dimensionOfMultiplication(numberOfRowsA,numberOfColumnsA,numberOfRowsB,numberOfColumnsB):
    x=numberOfRowsA
    y=numberOfColumnsB
    if numberOfRowsB==numberOfColumnsA:
        print("Dimension of multiplicative matrix would be {} by {}".format(x,y))
    else:
        print("these matrix ca not be multiplied")

def dimensionOfsum(numberOfRowsA,numberOfColumnsA,numberOfRowsB,numberOfColumnsB):
    x=numberOfRowsA
    y=numberOfColumnsB
    print("Dimension of multiplicative matrix would be {} by {}".format(x,y))

def check_inverse(matrix,numberOfRowsA,numberOfColumnsA):
    mat=[]
    for i in range(numberOfRowsA):
        for j in range(numberOfColumnsA):
            mat.append(matrix[i][j])
    determinant=(mat[0]*mat[3]) - (mat[1]*mat[2])
    d=mat[3]
    b=-(mat[1])
    a=mat[0]
    c=-(mat[2])
    adjoint=[]
    one=[]
    two=[]
    one.append(d)
    one.append(b)
    two.append(c)
    two.append(a)
    adjoint.append(one)
    adjoint.append(two)
    inverse=[]
    for c in range(numberOfRowsA):
        r=[]
        for k in range(numberOfColumnsA):
            x=adjoint[c][k] /determinant
            k += 1
            r.append(x)
        inverse.append(r)

    print(inverse)

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

def rows_interchange(matrix,first_row,Second_row):
    y=matrix[first_row]
    z=matrix[Second_row]
    matrix.insert(first_row,z)
    matrix.remove(matrix[first_row+1])
    matrix.insert(Second_row,y)
    matrix.pop(Second_row+1)
    return(matrix)

def matrix_multiplication(A,B,length):
    first_row=[A[0]]
    second_row=[A[1]]
    first_coloumn=[B[0][0],B[1][0]]  #i.0
    second_coloumn=[B[0][1],B[1][1]]  #1.i
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    for i in range(length):
        x=first_row[i]*first_coloumn[i]
        sum1=sum1+x
    for i in range(length):
        x=first_row[i]*second_coloumn[i]
        sum2=sum2+x
    for i in range(length):
        x=second_row[i]*first_coloumn[i]
        sum3=sum3+x
    for i in range(length):
        x=second_row[i]*second_coloumn[i]
        sum4=sum4+x

    r1=[sum1,sum2]
    r2=[sum3,sum4]
    a=[r1,r2]
    return(a)

def matrix_table(A,B,x,y):                  # A is the input matrix B is the matrix of the elemnets to be multiplied with  x and y are the lengths
    x1=[['N','10*N','100*N','1000*N']]
    for c in range(x):
        r=[A[c]]
        for k in range(y):
            z=A[c] * B[k]                  
            r.append(z)
        x1.append(r)

check_unit(a,b,nrA,ncA,nrB,ncB)

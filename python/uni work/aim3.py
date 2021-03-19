n=int(input("Enter the number  to print the table !!!   "))
a=[]
for i in range(1,n+1):
    a.append(i)
b=[10,100,100]
la=len(a)
lb=len(b)

def matrix_table(A,B,x,y):                  # A is the input matrix B is the matrix of the elemnets to be multiplied with  x and y are the lengths
    x1=[['N','10*N','100*N','1000*N']]
    for c in range(x):
        r=[A[c]]
        for k in range(y):
            z=A[c] * B[k]                  
            r.append(z)
        x1.append(r)
    return(x1)

def output(matrix,length,elements):
    for w in range(length):
        for i in range(elements):
            print(matrix[w][i], end="       ")
        print("\n")

elements=len(matrix_table(a,b,la,lb)[0])
matrix=matrix_table(a,b,la,lb)
l=len(matrix_table(a,b,la,lb))
output(matrix,l,elements)

x=int(input("Enter length of first square matrix  A     "))
first=[]
def matrix_input(length,matrix):
    for i in range(length):
        a=[]
        for z in range(length):
            word=("Enter an element [{}] [{}]  :   ").format(i,z)
            r=int(input(word))
            a.append(r)
        matrix.append(a)

y=int(input("Enter length of second square matrix B     "))
second=[]

def output(matrix,lengthR,lengthC):
    for w in range(lengthR):
        for i in range(lengthC):
            print(matrix[w][i], end="    ")
        print("\n")


matrix_input(x,first)
print("Matrix A is :")
output(first,x,x)

matrix_input(y,second)
print("Matrix b is :")
output(second,y,y)

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





print("MARTIX MULTIPLICATION  IS   !!!")

matrix=matrix_multiplication(first,second,x)
lr=len(matrix)
lc=len(matrix[0])

output(matrix,lr,lc)
#rows=len(matrix)
#coloumns=len(matrix[0])
#output(matrix,rows,coloumns)


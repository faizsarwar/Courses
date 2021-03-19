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

def output(matrix,length):
    for w in range(length):
        for i in range(length):
            print(matrix[w][i], end="    ")
        print("\n")


matrix_input(x,first)
print("Matrix A is :")
output(first,x)

matrix_input(y,second)
print("Matrix b is :")
output(second,y)

def matrix_addition(A,B,length):
    c=[]
    for i in range(length):
        for k in range(length):
            w=A[i][k]+B[i][k]
            c.append(w)
        

if len(x)==len(y):
    print("THE ADDITION IS   !!!")
    output(matrix_addition(first,second,x),y)
else:
    print("  ADDITION IS NOT POSSIBLE !!  ")
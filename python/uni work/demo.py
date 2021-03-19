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
b=matrixInput(numberOfRows=nrB,numberOfColumns=ncB,message=' B    ')

output(a,nrA,ncA,message=": A")
output(b,nrB,ncB,message=": B")






















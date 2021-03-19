a=0
l=[]
for i in range(1000):
    x=input("Enter a number !!!  ")
    if x =='done':
        break
    else:
        while True:
            try:
                x = int(x)
                l.append(x)
                break
            except ValueError:
                print("invalid input please enter again!!")
                break
l.sort()
largest=l[-1]
smallest=l[0]
print("largest number is {} and smallest number is {}".format(largest,smallest))
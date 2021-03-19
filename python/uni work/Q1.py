c=0
s=0
for i in range(1000):
    x=input("Enter a number  !!  ")
    if x =='done':
        break
    else:
        while True:
            try:
                x = int(x)
                s=s+x
                break
            except ValueError:
                print("invalid input please enter again!!")
                break
    c=c + 1
    average =float(s/c)
print("total is {} and average is {}".format(s,average))

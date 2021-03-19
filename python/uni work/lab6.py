sum=0
i=2
while i <2000000:
    c=0
    if i>2 and i%2==0:
        c=1
    else:
        j=3
        while j<=int(i**0.5):
            if i % j==0:
                c=1
            else:
                j=j+1
        if c==0:
            sum=sum+i
    i=i+1
print("the sum of pime numbers below 2 million is {}".format(sum))
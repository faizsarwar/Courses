# half-interval method  OR bisector method
a=float(input("Enter lower limit of the range in which solution lies"))
b=float(input("Enter upper limit of the range in which solution lies"))

x=a

fa = x**2 + 3*x - 10
               # agr equation ka derivative leke usmay kisi point ka x put krien tu us point pe tangent ka slope ajata hai. 
                                    
x=b
                                    #code for finding a point where y=0 where (fa,fb,fb) is equation of line
fb = x**2 + 3*x - 10

f= fa*fb

if (f>0):
    print("the graph of the equation Does not lie between the range!!")
else:
    fc=1
    k=1
    while (fc!=0):
        c=(a+b)/2    
        x=c
        fc = x**2 + 3*x - 10
        f=fa*fc
        print("counter={}     a={}    b={}   c={}".format(k,a,b,c))
        if (f<0):
            b=c
        else:
            a=c
        k+=1
        print("the solution of given equation is {}".format(c))

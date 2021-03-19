x=[]
for i in range(13):
    s=int(input("ENTER {} NUMBER!!!!    ".format(i+1)))
    x.append(s)
check_digit=x.pop(12)
Sum=0
    else:
        w=i[x]*3
    print(w)
    Sum=Sum+w
print(Sum)
check_number=10-(Sum/10)
if check_digit==check_number:
    print("number is correct")
else:
    print("Invalid number")
for i in range(12):
    if i%2==0:
        w=x[i]*1
    else:
        w=x[i]*3
    print(w)
    Sum=Sum+w
check_number=10-(Sum/10)
if check_digit==check_number:
    print("number is correct")
else:
    print("Invalid number")
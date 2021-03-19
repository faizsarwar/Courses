z=open("//home//faiz//python//table.csv","r")  #  csv file (excel files) aur (html) files bhi open kr sktay hain (json files bhi lkn json ka module import krwana parega) 
a=z.readlines()
for i in a[1:]:
    x=i.split(",")
    b=int(x[0])
    a=int(x[1])
    y="The square of '{}' is '{}' ".format(a,b)
    print(y)
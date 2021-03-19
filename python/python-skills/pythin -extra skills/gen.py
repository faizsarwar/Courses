# generators 

### Example #1

# def topten():           # iter aur next ka function nhi bnana parega direct hujaiga yield k keyword sai. class nhi banani paregii 
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5


# values =topten()

# print(values.__next__())

# for i in values:    # remaining values print krega kiunkay 1 pehlay hi print huchuka hai
#     print(i)


### example #2    ---------- > printing table

def topten():
    n=1 
    while n<=10:
        s=n*n
        yield s
        n+=1
    
values = topten()
for i in values:
    print(i)
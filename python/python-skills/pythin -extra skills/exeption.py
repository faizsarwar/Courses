# a=int(input(" Enter a number!!        "))
# b=int(input(" Enter a number!!        "))
# try:                # agr error nhi aya tu ye block chalegaa
#     print(a/b)
# except Exception:   # wrna ye block chalega
#     print("hey you cannot do divison by zero it is not possible")
# print("Bye")


                                    #####agr error bhi print hu to

a=int(input(" Enter a number!!        "))
b=int(input(" Enter a number!!        "))
try:               # try ka block jhn tk sahi huga whn tk chalega error k baad exception k block mai jaiga
    print(a/b)
except Exception as e:  
    print("hey you cannot do divison by zero it is not possible",   e)
finally:           # finally ka block zaror chalega upr wala koi bhi block chaley
    print("resource closed")
print("Bye")
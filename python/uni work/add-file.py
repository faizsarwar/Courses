f=open("//home//faiz//python//word.txt","w")  # 'W' say write huga 'r' say read huga 'x' say create aur write huga "a" say append huga.  
f.write("hello from python")
f.write("/n Hi programmer")                  #write k function chalanay say porana data loss hujaiga aur programm wala save hujaiga
f=open("//home//faiz//python//word.txt","r")
print(type(f))
print(f.read(3))
f.close()
f=open("//home//faiz//python//word.txt","r")
print(f.readlines())
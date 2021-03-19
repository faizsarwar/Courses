x=open('abc.html','w')
x.write('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body> <table> ')
for i in range(11):
    w=str(i*i)
    str(i)
    x.write("<tr><td>{}</td> <td>{}</td> </tr>".format(i,w))
    int(i)
x.write("""    </table> 
</body>
</html>""")

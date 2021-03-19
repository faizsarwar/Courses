import re 
pattern= re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-z]+")
text="faizsarwar44@gmail.com,faizsarwar856@yahoo.com, walii"
result= pattern.findall(text)
print(result)
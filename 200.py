import re
pattern=r"^abc"
mystring="abcdef"
x=re.match(pattern,mystring)
print(x)

import re
str1="Learnvern Provide Free Online Training"
print("Before Replace:",str1)
result=re.sub(r"[a-z]","0",str1)
print("After Replace:",result)
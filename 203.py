import re
str1="Learnvern provide free online training"
print("Before Replace:",str1)
result=re.sub(r"Provide","python",str1)
print("After Replace:",result)
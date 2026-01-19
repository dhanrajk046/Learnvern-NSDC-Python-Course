import re
txt="We are learning python"
x=re.search("\s",txt)
print("The first whitespaces:",x.start())

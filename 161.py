s="This is my file handling program"
file=open("demo.txt","w")
file.write(s)
print("file created")
file.close()
file=open("demo.txt","r")
filecontent = file.read()
print(filecontent)
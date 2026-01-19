try:
    a=int(input("Enter the value of A:"))
    b=int(input("Enter the value of B:"))
    c=a/b
    print("Answer:",c)
except Exception as e:
    print("Exception Caught:",e)
print("Bye")
p=int(input("Enter your percentage: "))
if p>70:
    print("A")
elif p>65 and p<=70:
    print("B+")
elif p>60 and p<=65:
    print("B")
elif p>55 and p<=60:
    print("C")
else:
    print("Fail")
age=int(input("Enter your age: "))
weg=int(input("Enter your weight in kg: "))

if age>=18:
    if weg>=50:
        print("Blood Donate")
    
    else:
        print("under weight")
else:
    print("under age")
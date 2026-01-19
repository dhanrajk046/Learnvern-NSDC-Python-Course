try:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number"))
    print("Both are valid integers.")
    total=num1+num2
    print("Sum=",total)
    print("Binary of sum=",bin(total))
except ValueError:
    print("Invalid input! Please enter integers only.")
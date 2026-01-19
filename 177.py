try:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
except ValueError:
    print("Invalid input! Please enter integers only.")
else:
    print("Both inputs are valid integers.")
    print("Sum=",num1+num2)
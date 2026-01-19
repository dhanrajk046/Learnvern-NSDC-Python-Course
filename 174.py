try:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    print("Both numbers are valid integers.")
    print("first number:",num1)
    print("second number:",num2)
except ValueError:
    print("Invalid input! Please enter integers only.")
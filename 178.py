try:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    result=num1/num2
    print("Result=",result)
except ValueError:
    print("Error: Please enter valid integers only.")
except ZeroDivisionError:
    print("Error; Divison by zero is not allowed.")
except Exception as e:
    print("Some other error occured:",e)
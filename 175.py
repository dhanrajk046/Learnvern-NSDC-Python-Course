try:
    user_input=input("Enter a string(expression):")
    result=eval(user_input)
    print("The evaluated result is:",result)
except Exception as e:
    print("Invalid input! Error:",e)
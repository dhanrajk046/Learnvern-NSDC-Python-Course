try:
    print(x)
except NameError:
    print("Variable is not defined:")
except:
    print("Exception Caught")
class MyException(Exception):
    pass

c = 25
try:
    if c > 5:
        raise MyException("Something went wrong")
except MyException as e:
    print(f"Caught custom exception:  {e}")

print("Program continues after exception handling.")                                                                                                                                                     
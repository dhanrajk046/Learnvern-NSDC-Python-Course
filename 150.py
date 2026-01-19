def Calculation_basis(a, b):
    addition = a + b
    subtraction = a - b
    if b != 0:
        division = a / b
    else:
        division = "undefined (division by zero)"
    return addition, subtraction, division


x, y = 10, 5
result = Calculation_basis(x, y)
print("Addition:", result[0])
print("Subtraction:", result[1])
print("Division:", result[2])
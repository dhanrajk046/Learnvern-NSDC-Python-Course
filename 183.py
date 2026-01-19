class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunction(self):
        print("My Name is: " + self.name)


m1 = MyClass("Sunit", 25)
m1.myfunction()  # call the method
print("Age:", m1.age)  # print the age attribute
m1.name
m1.age = 26
print("Age:", m1.age)
del m1.age
try:
    print("Age:", m1.age)
except AttributeError:
    print("Age: attribute has been deleted")

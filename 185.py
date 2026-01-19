class A:
    def myfunction(self):
        print("Class A function called")

class B(A):
    def myfunction2(self):
        print("Class B function called")

class C(B):
    def myfunction3(self):
        print("Class c function called")

c1=C()
c1.myfunction()
c1.myfunction2()
c1.myfunction3()
class A1:
    def myfunction1(self):
        print("Class A1 function called")

class B1:
    def myfunction2(Self):
        print("Class B1 function called")

class C1(A1,B1):
    def myfunction3(self):
        print("Class C1 function called")

c1=C1()
c1.myfunction1()
c1.myfunction2()
c1.myfunction3()
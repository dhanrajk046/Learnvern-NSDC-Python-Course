class A1:
    def myfunction1(self):
        print("Class A1 Function Called")


class A2(A1):
    def myfunction2(self):
        print("Class A2 Function Called")


class A3(A1):
    def myfunction3(self):
        print("Class A3 function Called")


a2 = A2()
a3 = A3()
a2.myfunction1()  # inherited from A1
a2.myfunction2()
a3.myfunction1()  # inherited from A1
a3.myfunction3()
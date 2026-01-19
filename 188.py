class B1:
    def myfunction1(self):
        print("function of class B1")


class B2(B1):
    def myfunction2(self):
        print("function of class B2")


class B3(B1):
    def myfunction3(self):
        print("function of class B3")


class B4(B2, B3):
    def myfunction4(self):
        print("function of class B4")


b = B4()
b.myfunction1()
b.myfunction2()
b.myfunction3()
b.myfunction4()
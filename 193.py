class A:
    def __init__(self, a):
        self.__a
    def show(self):
        print("Private Variable:",self.__a)
class B(A):
    def __init__(self, b):
        super().__init__(b)
    def showB(self):
        print(self.__a)

obj=B(20)
obj.showB()                                                                                                                                                                  
class A:
    def __init__(self, a):
        # use a single leading underscore for a 'protected' attribute
        self._a = a

    def show(self):
        print("Protected Variable:", self._a)
class B(A):
    def __init__(self, b):
        super().__init__(b)

    def showB(self):
        # subclass can access the protected attribute
        print("Variable Value:", self._a)


if __name__ == "__main__":
    obj = B(30)
    # call method from A
    obj.show()
    # call method from B
    obj.showB()

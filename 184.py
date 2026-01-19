class Parentclass:
    def myfunction1(self):
        print("Parent class function Called")

class childclass(Parentclass):
    def myfunction2(self):
        print("child class function called")

c1=childclass()
c1.myfunction1()
c1.myfunction2()
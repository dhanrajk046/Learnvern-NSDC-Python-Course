class MO1:
    def myfunction(self,a):
        print("Class MO1 function called")
    
class MO2(MO1):
    def myfunction(self,a):
        print("Class MO2 function called")
        super().myfunction(10)

class MO3(MO2):
    def myfunction(self,a):
        print("Class MO3 function called")
        super().myfunction(10)

m=MO3()
m.myfunction(10)
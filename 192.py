class Animal:
    def move(self):
        pass
class Dog(Animal):
    def move(self):
        print("I can bark")
class Snake(Animal):
    def move(self):
        print("I can hiss")

d=Dog()
s=Snake()
d.move()
s.move()
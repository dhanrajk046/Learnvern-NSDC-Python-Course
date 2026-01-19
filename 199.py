class Vehicle:
    def start(self):
        print("Vehicle is starting...")
    def stop(self):
        print("Vehicle is stopping...")
class Car(Vehicle):
    def honk(self):
        print("Car is honking...")
c=Car()
c.start()
c.honk()
c.stop()
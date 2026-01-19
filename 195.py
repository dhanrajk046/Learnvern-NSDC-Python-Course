class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display_info(self):
        print(f"Vehicle brand:{self.brand},Model:{self.model}")
car=Vehicle("Tesla","Model S")
car.display_info()

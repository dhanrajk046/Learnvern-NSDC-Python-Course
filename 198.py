class Vehicle:
    def start(self,*args):
        if len(args)==0:
            print("starting Vehicle...")
        elif len(args)==1:
            print(f"starting vehicle with key:{args[0]}")
        elif len(args)==2:
            print(f"starting vehicle with key:{args[0]} and mode:{args[1]}")
        else:
            print("Too many arguments provided")
            
class Bus(Vehicle):
    pass

b=Bus()
b.start()
b.start("SmartKey")
b.start("SmartKey","Automatic")
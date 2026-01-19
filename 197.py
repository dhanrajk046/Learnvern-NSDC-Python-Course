class Vehicle:
    def start(self,*args):
        if len(args)==0:
            print("starting vehicle...")
        elif len(args)==1:
            print(f"starting vehicle with key:{args[0]}")
        elif len(args)==2:
            print(f"starting vehicle with key:{args[0]} and mode:{args[1]}")
        else:
            print("Too many arguments provided!")
v=Vehicle()
v.start()
v.start("smart key")
v.start("smart key","Automatic")

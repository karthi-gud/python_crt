#single level inheritance ## normal method and static method 

class vehicle:
    def __init__(self):
        print("im the vehicle class constructor ")
    @staticmethod
    def Start():
        print("vehicle is started ")

class car(vehicle):
    def __init__(self):
        super().__init__()
        print("im the car class constructor")
    @staticmethod
    def Start():
        vehicle.Start()  # Call the parent static method directly
        print("car is started ")
    def display(self):
        print("im the car class display method")

c1 = car()
c1.display()
c1.Start()
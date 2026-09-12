class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Engine:
    def start(self,type):
        print(f"{type} engine started")

class Car(Vehicle):
    def __init__(self):
        self.engine = Engine()
        # self.engine.start("Diesel")
    def start(self,type):
        self.engine.start(type)

car = Car()
car.move()
car.start("Diesel")
car2 = Car()
car2.start("Petrol")
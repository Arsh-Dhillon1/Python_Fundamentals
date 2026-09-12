from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        print("Hello")

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Boom Boom")
        super().start()

    def stop(self):
        print("Stop the Car Bro")

c = Car()
c.start() 
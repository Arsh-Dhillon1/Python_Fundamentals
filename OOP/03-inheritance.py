class Person:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city

    def speak(self):
        print(f"Hello my name is {self.name}")

class Employee(Person):
    pass

class Manager(Person):
    pass

e1 = Employee("Arsh", "21.4", "Phagwara")
m1 = Manager("Bonzo",1, "Bathinda")

e1.speak()
m1.speak()
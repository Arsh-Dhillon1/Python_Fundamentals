class Prey():
    def flee(self):
        print("This animal is fleeing")

class Predator():
    def flee(self):
        print("This animals is hunting")

class Fish(Prey,Predator):
    pass

f = Fish()
f.flee()
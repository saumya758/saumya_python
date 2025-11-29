class Vehicle:
    def calculate_fare(self, km):
        pass

class Auto(Vehicle):
    def calculate_fare(self, km):
        return km * 8

class Bike(Vehicle):
    def calculate_fare(self, km):
        return km * 6

class Sedan(Vehicle):
    def calculate_fare(self, km):
        return km * 12

vehicles = [Auto(), Bike(), Sedan()]
for v in vehicles:
    print(v.calculate_fare(10))

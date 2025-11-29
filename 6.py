class Staff:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show(self):
        print(self.name, self.id)

class Doctor(Staff):
    def duty(self):
        print("Doctor treats patients")

class Nurse(Staff):
    def duty(self):
        print("Nurse provides care")

class Surgeon(Staff):
    def duty(self):
        print("Surgeon performs operations")

class LabTech(Staff):
    def duty(self):
        print("Lab Technician performs tests")

staff = [Doctor("A", 1), Nurse("B", 2), Surgeon("C", 3)]
for s in staff:
    s.show()
    s.duty()

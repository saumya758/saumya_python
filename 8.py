class Student:
    def __init__(self, name, marks, leaves, discipline):
        self.name = name
        self.__marks = marks
        self.__leaves = leaves
        self.__discipline = discipline

    def get_marks(self, role):
        if role == "faculty":
            return self.__marks
        return "Access Denied"

    def update_marks(self, new_marks, role):
        if role == "faculty":
            self.__marks = new_marks

s = Student("Rohan", 80, 2, "Good")
print(s.get_marks("faculty"))

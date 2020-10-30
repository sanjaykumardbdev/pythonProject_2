# inner class:
class Student:
    def __init__(self, name, rollno):
        self.fname = name
        self.rollcode = rollno
        # if you  want to create obj inside class
        self.lap = self.Laptop()

    def show(self):
        print(self.fname, self.rollcode)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('san', 23)
s2 = Student('sanjay', 23)
s1.show()
s2.show()

# in case, if you don't want to create obj inside class
#lap1 = Student.Laptop()
#lap1.show()
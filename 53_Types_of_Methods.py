# instance method
# class method      variable
# static method     variable

# in case of var, class n static var are same but difnt in case of method
class Student:
    #static or class var : outside var
    school = "Telusko"
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    # instance method
    def agv(self):
        return (self.m1 + self.m2 + self.m3)/3

    # instance itself have to type of method: accessor, mutators
    # accessor : fetch value , mutators: set the value
    def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1 = value

    #classmethod  use decorator to access class var
    @classmethod
    def getSchool(cls):
        return cls.school
    # static method: in case if you don't want to relate with any class or obj.
    # this method nothing to do with instance or class variable

    @staticmethod
    def info():
        print("this is student class.. in abc ")

s1 = Student(34, 47, 32)
s2 = Student(89, 32, 12)
print('using get ', s1.get_m1())
s1.set_m1(100)
print('using get ', s1.get_m1())

# avg is instance method becoz it called with object
print(s1.agv())
print(s2.agv())
print("-----------------------")
print(s1.getSchool())
print(Student.getSchool())

Student.info();


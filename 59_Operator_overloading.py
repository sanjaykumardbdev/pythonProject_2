#59 Python Tutorial for Beginners | Operator Overloading | Polymorphism

a = 5
b = 6
print(a+b)
print(int.__add__(a, b))

a = '5'
b = '6'
print(a+b)
print(str.__add__(a, b))

print(a.__str__())      # when u r calling print(a) behind it is calling like this : print(a.__str__())

print('-----------------------------')
class Student:
    def __init__(self, m1, m2):
        self.mk1 = m1
        self.mk2 = m2

    def __add__(self, other):
        m1 = self.mk1 + other.mk1
        m2 = self.mk2 + other.mk2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):
        #s1 = self.mk1 + other.mk1
        #s2 = self.mk2 + other.mk2

        s1 = self.mk1 + self.mk2
        s2 = other.mk1 + other.mk2

        if s1 > s2:
            return True
        else:
            return False

    def __str__(self):
        #print(self.mk1, self.mk2)
        return( '{}   {}'.format(self.mk1, self.mk2))


s1 = Student(30, 3)
s2 = Student(3, 3)

print("Str overloading----------------------------------")
print()

print(s1.__str__())
print(s2.__str__())

print()
print("Done----------------------------------")


# Student.__add__(s1,s2)
s3 = s1 + s2
print(s3.mk1)

s4 = s1 + s2
print(s4.mk2)

if s1 > s2:
    print('s1 Wins')
else:
    print('s2 wins')

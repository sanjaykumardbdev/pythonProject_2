# method Overriding not supported in python, so using trick
# : 2 method with same name but different parameter
# method Overriding: inheritance class a and b: both have same method with same no. of parameter called overriding

class Student:
    #def sum(self,a,b,c):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        s = self.a + self.b + self.c
        p = a+b+c
        print('in init', s)
        print('p value', p)
s1 = Student(12, 12, 12)

print('-------------------------------')


class Student1:
    def __init__(self, a1, b1):
        self.a = a1
        self.b = b1

    s = 0
    def sum(self,a=None, b=None, c=None):

        if a!=None and b!= None and c!=None:
            s = a+b+c
        elif a != None and b!= None:
            s = a + b
        else:
            s = a

        return s


s1 = Student1(12,12)

print(s1.sum(3))
print(s1.sum(3,3))
print(s1.sum(3,3,3))


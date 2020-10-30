#inheritance
# constructor / MRO
class A:
    def __init__(self):
        print('In A Init')
    def feature1(self):
        print('feature1 working')
    def feature2(self):
        print("feature2 working")

#B is subclass and A is super class
class B(A):
    # first it will look init of B, if not then it will go for init of A
    def __init__(self):
        # in case, you wan to print class A constructor.
        super().__init__()
        print('In B Int')
    def feature3(self):
        print('feature3 working')
    def feature4(self):
        print("feature4 working")

class C():
    def feature5(self):
        print('feature 5 working')


print("-------------------")
a1 = A()
a1.feature1()
a1.feature2()

print("--Multi Level Inheritance-----------------")
b1 = B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

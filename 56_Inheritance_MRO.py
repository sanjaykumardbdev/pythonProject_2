#inheritance
# constructor / MRO
class A:
    def __init__(self):
        print('In A Init')
    def feature1(self):
        print('feature1 A working')
    def feature2(self):
        print("feature2 working")

#B is subclass and A is super class
class B():
    # first it will look init of B, if not then it will go for init of A
    def __init__(self):
        print('In B Int')
    def feature1(self):
        print('feature3 B working')
    def feature2(self):
        print("feature4 working")

class C(A,B):
    def __init__(self):
        # MRO: method resolution order: starts from left to right
        super().__init__()
        print('In C Int')
    def feature5(self):
        print('feature 5 working')

    def feat(self):
        super().feature1()

print("--Multi Level Inheritance-----------------")
c1 = C()
# again MRO: method resolution order.
print('------------------------')
c1.feature1()
print('------------------------')
c1.feat()

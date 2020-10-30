class A:
    def __init__(self, x):
        self.m = x

    # this is how can add obj
    def __add__(self, other):
        return self.m * other.n

class B:
    def __init__(self, y):
        self.n = y

a1 = A(20)
b1 = B(20)


print(a1 + b1)      # A.__add__(a,b)

print('------------------------')
print(10+10)               # int.__add__(10,10)
print('a' + 'b')           # str.__add__('a','b')



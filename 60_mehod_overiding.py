# method Overriding: inheritance class a and b: both have same method with same no. of parameter called overriding

class A:
    def show(self):
        print("in A Show")


class B(A):
    def show(self):
        print("in B Show")

a1 = B()
a1.show()
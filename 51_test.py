class Computer:
    def __init__(self):
        self.name = "sanjay"
        self.age = 28

    # why self:
    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False



c1 = Computer()
c2 = Computer()


c1.name = 'jay'
c1.update()
print('c1 age ', c1.age)

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")


# we are calling c1 but how pointer will know which obj you want to call
# c1.update()-> we are passing c1 in bracket so self will be assigned to c1
# c1.update()
# print(c1.name)
# print(c2.name)

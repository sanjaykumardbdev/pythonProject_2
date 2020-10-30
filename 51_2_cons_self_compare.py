class computer:
    def __init__(self):
        self.name = 'san'
        self.age = 25

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = computer()
c2 = computer()
c2.name = "jay"
c2.age = 25
# compare(who is calling, whom to compare
if c1.compare(c2):
    print("They are same")
else:
    print("They are not same")

print(c1.name, c1.age)
print(c2.name, c2.age)

print("--------------------------------------------------")

class computer:
    def __init__(self):
        self.name = 'san'
        self.age = 25
    def update(self):
        self.age = 30

c1 = computer()
c2 = computer()

c1.name = "jay"
c1.age = 26

c1.update()
print(c1.name, c1.age)
print(c2.name, c2.age)

print("--------------------------------------------------")


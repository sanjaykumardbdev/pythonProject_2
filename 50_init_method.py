# special: variable: __name__ , method: __init__
class computer:
    # kind of constructor
    def __init__(self, cpu, ram):
        print("In Init")
        self.cpu1 = cpu
        self.ram1 = ram

    def config(self):
        print("config is =", self.cpu1, self.ram1 )

    def config2(self):
        print("config2 is =", self.cpu1, self.ram1)


comp1 = computer('i5',16)
comp2 = computer('i7',32)

comp1.config()
comp2.config2()

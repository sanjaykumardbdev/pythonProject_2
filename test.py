class Computer:
    def __init__(self, cpu, ram):
        self.processor = cpu
        self.memory = ram
        print("processor : {} , Memory : {}".format(self.processor, self.memory))

    def config(self):
        print('i5 16gb 1tb')


# object creation
# pass all req parameter while creating obj
com1 = Computer('i5', 16)

# passing obj to method config of class computer:
#Computer.config((com1))

# passing com1 as parameter to config method, com1 belongs to computer class
#com1.config()

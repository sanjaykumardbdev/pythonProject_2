# duck typing:  like interface:

class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self, ide):
        ide.execute()

#ide = PyCharm()
ide = MyEditor()

lap1 = Laptop()
# passing an obj of class to another class:
lap1.code(ide)

#Note: if there is an obj which has ide and it has method execute thats it.
# we are not concern about which class it is, only execute method should be there.


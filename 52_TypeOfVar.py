# instant n class(static) variable:
# namespace is an area where you create and store obj/var
# class namespace and obj/instance namspace
class car:
    wheel = 4               # var belongs to class namespace/ class or steady var:
    def __init__(self):
        self.comp = "BMW"   # var belongs to instance/obj namespace
        self.mil = 10

c1 = car()
c2 = car()
c1.mil = 8
car.wheel = 5               # it will affect all the obj which are using it as it is shared bet all obj.

print("comp: {} mil: {} Wheel {}".format(c1.comp, c1.mil, c1.wheel))
print("comp: {} Mil: {} Wheel {}".format(c2.comp, c2.mil, c1.wheel))

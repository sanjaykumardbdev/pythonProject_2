# in iterator, we need to define fucntion next and iter.
# in python: if you don't want to define itterator then use generator
# generator will give itterator:
# yeild is special function which will make your function as generator.
# generator gives you an itterator

def topten():
    # using yield will return in format of itterator.
    # it is generator since it gives a iterator, can write multiple yield
    yield 1
    yield 2
    yield 3
    yield 4

    # can use return which will fuction same as before
    # return 3


values = topten()
# print(values)

# to fetch value from itteraor need to use __next__ function

print(values.__next__())
print(next(values))

for i in values:
    print(i)

print('--------------------------')


def topsquare():
    n = 1
    while n <= 10:
        print('sqaure of ', n)
        sq = n * n
        yield sq
        n += 1


values = topsquare()
for i in values:
    print(i)

print('--------------------------')


class test:
    def sqr(self, n):
        return n * n


tt = test()
k = tt.sqr(5)
print(k)


print('--------------------------')

test1 = test()
kk = test1.sqr(10)
print(kk)

print('--------------------------')

test2 = test()
print(test2.sqr(12))




print('--------for loop ------------------')

class test:

    def sqr(self, n):
        return n * n

    def calc(self):
        for i in range(11):
            k1 = self.sqr(i)
            print(k1)

tt = test()
k = tt.sqr(5)
print(k)

k1 = tt.calc()
print(k1)


print('--------while loop ------------------')

class test1:

    def sqr(self, n):
        return n * n

    def calc1(self):
        i =1
        while i <= 10:
            k = i * i
            print(i, '*',i, '=', k)
            i+=1

tt = test1()
k = tt.sqr(5)
print(k)

k1 = tt.calc1()
print(k1)

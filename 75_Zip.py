names = ("Navin", "Kiran", "harsh","navin","Navin")
comps = ("Dell", "Apple", "MS","dell","Dell")

zipped = zip(names,comps)
print(zipped)


lst = list(zip(names,comps))
print(lst)

print('---------------------------')
set1 = set(zip(names,comps))
print(set1)


print('---------------------------')
dict1 = dict(zip(names,comps))
print(dict1)

print('---------------------------')
print('---------------------------')
for (a, b) in zipped:
    print(a, b)

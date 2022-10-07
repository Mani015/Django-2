x = {1,2,3,4,5}
print(type(x))
# <class 'set'>

y = frozenset(x)
print(y)
# frozenset({1, 2, 3, 4, 5})

print(type(y))
# <class 'frozenset'>

y.add(10)
#print(y)

# AttributeError: 'frozenset' object has no attribute 'add'
y.remove(2)
#print(y)

#AttributeError: 'frozenset' object has no attribute 'add'
x = {1,2,3,4,5}
print(x)
#{1, 2, 3, 4, 5}

y = frozenset(x)
print(y)
#  frozenset({1, 2, 3, 4, 5})

x.add(y)
print(x)
#  {frozenset({1, 2, 3, 4, 5}), 1, 2, 3, 4, 5}

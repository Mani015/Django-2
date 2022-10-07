s = {1, 2, 3, 4, 5}
#print(s[0])
# TypeError: 'set' object is not subscriptable

s1 = {1, 2, 3, 4, 5}
#print(s1[0:5])
#TypeError: 'set' object is not subscriptable

s2 = {1, 2, 3, 4, 5}
print(s2 * 3)
# TypeError: unsupported operand type(s) for *: 'set' and 'int'
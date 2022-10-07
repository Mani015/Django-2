# set

s = {1,2,3,4,5,6, 1,2, "A", "B", "C", "B", 10.0, 12.0, True, False, False}
print(s)
print(type(s))
#<class 'set'>

s.update([40,50])
print(s)
#{False, 1, 2, 3, 4, 5, 6, 40, 10.0, 12.0, 'C', 'B', 50, 'A'}

s.remove(5)
print(s)
# {False, 1, 2, 3, 4, 6, 'B', 40, 'C', 10.0, 12.0, 50, 'A'}

s.add(60)
s.add(70)
s.add(80)
print(s)
# {False, 1, 2, 3, 4, 6, 'B', 40, 70, 'C', 10.0, 12.0, 'A', 80, 50, 60}
# Slicing
# string[start/begin : end(-1) : stepover(default value 1)]

lst = [1, 2, 3, 4, 5, 6, 7, 8]
#     -8,-7,-6,-5,-4,-3,-2,-1

print(lst[-1])
#8

print(lst[-1 : -5])
#[]

print(lst[-5 : -1])
#[4, 5, 6, 7]

print(lst[-8 : -1])
#[1, 2, 3, 4, 5, 6, 7]

print(lst[0]) # 1
print(lst[-8]) # 1

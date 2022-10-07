# Slicing
# string[start/begin : end(-1) : stepover(default value 1)]

lst = [1,2,3,4,5,6,7,8]
#      0,1,2,3,4,5,6,7
print(lst)
#  [1, 2, 3, 4, 5, 6, 7, 8]

#Index call
print(lst[4]) # 5

#Index start and end
print(lst[1 : 6])
# [2, 3, 4, 5, 6]

#Index start : total values...
print(lst[2:])
#[3, 4, 5, 6, 7, 8]

#index start optional and end is 5
print(lst[:5])
# [1, 2, 3, 4, 5]

#Copy or Total List Values using Slicing
print(lst[ : ])
# [1, 2, 3, 4, 5, 6, 7, 8]

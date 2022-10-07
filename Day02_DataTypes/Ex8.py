# printing list data
animals = ["tiger", "elephant", "camel"]
print(animals)  # ['tiger', 'elephant', 'camel']

# index
print(animals[0])  # tiger
print(animals[1])  # elephant
print(animals[2])  # camel

# length
print(len(animals)) # 3

# append
animals.append("rabbit")
print(animals)  # ['tiger', 'elephant', 'camel', 'rabbit']

# extend
animals.extend(["lion", "fox", "dog", "cat"])
print(animals)
# ['tiger', 'elephant', 'camel', 'rabbit', 'lion', 'fox', 'dog', 'cat']

# pop
animals.pop()
print(animals)
#  ['tiger', 'elephant', 'camel', 'rabbit', 'lion', 'fox', 'dog']

animals.pop()
print(animals)
#  ['tiger', 'elephant', 'camel', 'rabbit', 'lion', 'fox']

# pop with index
animals.pop(2)
print(animals)
#  ['tiger', 'elephant', 'rabbit', 'lion', 'fox']











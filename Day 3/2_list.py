# Python lists are mutable
# They are the sequence of elements enclosed within big brackets
# Unlike array, list elements can be heterogenous
# All sequential datatypes can be called as iterables

# Creating non-empty lists
a = [1, 2, 3]  # List of integers
b = ["a", "e", "i", "o", "u"]  # List of strings
c = [1, 2.2, "A", [1, 2], {3, 4}]
print(a)
print(b)
print(c)

d = list("abc")
print(d)  # ["a", "b", "c"]

# for i in a:
#     print(i)

# Creating empty lists
a = list()
a = []


# Accessing list elements
vowels = ["a", "e", "i", "o", "u"]
# list elements can be accessed using indexing and slicing
print(vowels[0]) # a
print(vowels[4]) # u 
print(vowels[10]) # Index Error
print(vowels[-2]) # o
print(vowels[-1]) # u
print(vowels[-10]) #Index Error

# Slicing
data = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "J"]
print(data[0:8])    # "a", "b", "c", "d", "e", "f", "g", "h",
print(data[2:7])    # "c", "d", "e", "f", "g"
print(data[7:3])    # empty list []
print(data[4:9])    # "e", "f", "g", "h", "i"
print(data[5:])     # "f", "g", "h", "i", "J"

print(data[-9:-2])  #"b", "c", "d", "e", "f", "g", "h"
print(data[-2: -8]) # empty list []
print(data[-3:])    # "h", "i", "J"
print(data[:-2])    # "a", "b", "c", "d", "e", "f", "g", "h"


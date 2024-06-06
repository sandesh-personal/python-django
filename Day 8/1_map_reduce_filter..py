# map(), reduce() and filter() are higher order functions
# in python

# map()
# map() function takes function as a first parameter and iterable as 
# second parameter
# The length of initial iterable and the final result is same when using map()



def add_ten(element):
    return element + 10
a = [1, 2, 3, 4]
result = list(map(add_ten, a))
print(result)


# filter()
# filter() also takes first parameter as function and second as an iterbale
# The length of initial iterable and the final result may not be same in filter

data = [1, 2, 3, 4, 5, 6, 7, 8]

def get_even(element):
    if element % 2 == 0:
        return True
    else:
        return False

result = list(filter(get_even, data))
print(result)


# reduce()
# reduce() also taks function as first paramerter and iterable as second parameter
data = [1, 2, 3, 4, 5]
result = sum(data)
print(result)

# Task
data = [1, 2, 3, 4, 5]
result = 1
for each in data:
    result = result * each
print(result)

# using reduce()
from functools import reduce

def multiply(x, y):
    return x*y

result = reduce(multiply, data)
print(result)
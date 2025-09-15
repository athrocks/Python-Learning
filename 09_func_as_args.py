# Functions as Arguments

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def operate(func, x, y):
    return func(x, y)

# Using the functions as arguments
result_add = operate(add, 5, 3)
print(f"Addition Result: {result_add}")

result_subtract = operate(subtract, 5, 3)
print(f"Subtraction Result: ",result_subtract)

# Lambda functions as arguments
def calculator(operation, n1, n2):
    return operation(n1, n2)  # Using the 'operation' argument as a function

# 10 and 20 are the arguments.
result = calculator(lambda n1, n2: n1 * n2, 10, 20)
print(result)

# The map Object
num_list = [0, 1, 2, 3, 4, 5]

squared_numbers = map(lambda num: num ** 2, num_list)
print(list(squared_numbers))  # Convert map object to list to see the results

# The reduce Object
# reduce(function, iterable[, initializer])
from functools import reduce
numbers = [1,2,3,4,5]
product = reduce(lambda x, y: x * y, numbers)
print(product) # Output: 120 (1*2*3*4*5)

# The filter object
# filter(function, iterable)
numList = [30,2,-15,4,5,-6,7,8,9]
positive_numbers = filter(lambda x: x > 0, numList)
print(positive_numbers) # op: <filter object at 0x000001F6D11074F0>
print(list(positive_numbers))
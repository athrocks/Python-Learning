# Lambda functions are small anonymous functions defined with the lambda keyword.
# They can take any number of arguments but can only have one expression.
# The expression is evaluated and returned.
# Syntax: lambda arguments: expression
triple = lambda num : num * 3
print(triple(5))


print_triple = lambda num : print(num * 3)
print_triple(10)

hardcoded_triple = lambda : 3 * 3
print(hardcoded_triple())

# Using conditional logic in lambda functions
is_Even = lambda num : True if num % 2 == 0 else False
print(is_Even(4))


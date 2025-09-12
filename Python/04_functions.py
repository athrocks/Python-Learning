def sayHello():
    print("Hello!")

def sayHelloTo(name):
    print("Hello,", name)
    return "Hello, " + name

sayHello()
greeting = sayHelloTo("Alice")
print(greeting)

def deeper():
    print('Now inside the function "deeper".')

def deep():
    print('Now inside the function "deep".')
    deeper()
    print('Back inside the function "deep".')

deep()


def getSum(a,b): # Definition of the function
  mysum = a + b # Adding a and b and assigning the result in variable mysum
  return mysum # returning mysum value

print(getSum(5,6))

# built in function explore by adding dot operator
print("abc".isdigit())
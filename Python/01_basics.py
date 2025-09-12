print("Hello World")

print("Single",end="")
print("Line")

# name=input("Enter your name: ")
# print("Hello", name)

# Data Types in Python
# int,float,string
persons = 5
totalWeight = 350.6
team="A"
print("Total weight of", persons, "persons of team",team, "is:",totalWeight, "kgs")

# Every input in python is a string
a=input("Enter a: ")
b=input("Enter b: ")
result = a+b
print(result)

# int input
a=int(input("Enter an integer: "))
b=int(input("Enter an integer: "))
print ("When we apply + operator it gives", a+b, "which is the sum of two integers!")

c=float(input("Enter floating point number: "))
print("c is: ",c)

age = int(input ("Enter your age: "))
if age>=18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote!")

# variable = 5+
# print(variable)

for a in [0,1,2,3,4]:
    print(a)
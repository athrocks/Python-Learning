class MyClass:
    pass

obj = MyClass()

print(type(obj))
print(obj)

class Employee:
    ID = 3789
    salary = 2500
    department = "HR"

Atharva = Employee()

print("ID: ", Atharva.ID)
print("Salary: ", Atharva.salary)
print("Department: ", Atharva.department)

Aditya = Employee()
Aditya.ID = 4587
Aditya.salary = 3000
Aditya.department = "IT"

# Creating a new property outside the class
Aditya.location = "Pune"

print("ID: ", Aditya.ID)
print("Salary: ", Aditya.salary)
print("Department: ", Aditya.department)
print("Location: ", Aditya.location)

class Employee:
    def __init__(self, ID, salary, department):
        self.ID = ID
        self.salary = salary
        self.department = department

Harsh = Employee(3789,2500,'IT')
print("Harsh object details:", Harsh.ID, Harsh.salary, Harsh.department)

class Player:
    teamName = 'Liverpool' # class variables
    def __init__(self, name):
        self.name = name # creating instance variables

p1 = Player('Mark')
p2 = Player('John')

class EmployeeDetails:
    def __init__(self,ID=None,salary=None,department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    def tax(self):
        return (0.2 * self.salary)
    
    def salaryPerDay(self):
        return (self.salary / 30)
    
Steve = EmployeeDetails(3789,2700,'IT')
print("Steve's tax:", Steve.tax())
print("Steve's salary per day:", Steve.salaryPerDay())

# Method Overloading
class DemoOverloading:
    def show(self, x=None):
        if x is not None:
            print("Value:", x)
        else:
            print("No value")

obj = DemoOverloading()
obj.show()      # No value
obj.show(10)    # Value: 10

# Class Methods
class MyClass:
    classVariable = 'educative'

    @classmethod
    def demo(cls):
        return cls.classVariable

class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * (self.radius ** 2)

    @classmethod
    def circleInfo(cls):
        return f"This is a circle class with pi value as {cls.pi}"
    
print(Circle.circleInfo()) # calling class method without creating object

# Static Methods
class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    @staticmethod
    def demo():
        print("I am a static method.")

p1 = Player('lol')
p1.demo()
Player.demo() # calling static method without creating object

# Access Modifiers
# Public Attributes
class Employee:
    def __init__(self, ID, salary):
        # all properties are public
        self.ID = ID
        self.salary = salary

    def displayID(self):
        print("ID:", self.ID)


Steve = Employee(3789, 2500)
Steve.displayID()
print(Steve.salary)

# Private Attributes & Methods
class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property since (double underscore) __ prefix

    def __displayID(self):  # displayID is a private method
        print("ID inside private function:", self.ID)

Steve = Employee(3789, 2500)
print("ID:", Steve.ID)

# this will cause an error
# print("Salary:", Steve.__salary)

# Accessing Private Attributes
print("Salary:", Steve._Employee__salary)  # This works

# Accessing Private Methods
# this will cause an error
# Steve.__displayID() 

Steve._Employee__displayID()  # This works
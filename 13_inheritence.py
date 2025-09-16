class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"Make: {self.make}, Model: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def display_info(self):
        vehicle_info = super().display_info()
        return f"{vehicle_info}, Doors: {self.doors}"

class Motorcycle(Vehicle):
    def __init__(self, make, model, cc):
        super().__init__(make, model)
        self.cc = cc

    def display_info(self):
        vehicle_info = super().display_info()
        return f"{vehicle_info}, CC: {self.cc}"

car = Car("Toyota", "Camry", 4)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 750)

print(car.display_info())          # Make: Toyota, Model: Camry, Doors: 4
print(motorcycle.display_info())   # Make: Harley-Davidson, Model: Street 750, CC: 750

# -------------------------------------------------------------------------------

# Single Inheritance
class Vehicle:
    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    def open_trunk(self):
        print("Trunk opened")

corolla = Car()
corolla.start_engine()  # Engine started
corolla.open_trunk()    # Trunk opened

# ------------------------------------------------------------------------------

# Multi Level Inheritance
class Vehicle:
    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    def open_trunk(self):
        print("Trunk opened")

class ElectricCar(Car):
    def charge_battery(self):
        print("Battery charging")

tesla = ElectricCar()
tesla.start_engine()    # Engine started
tesla.open_trunk()      # Trunk opened
tesla.charge_battery()  # Battery charging

# ------------------------------------------------------------------------------

# Hierarchical Inheritance
class Vehicle:
    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass

corolla = Car()
corolla.start_engine()  # Engine started

f150 = Truck()
f150.start_engine()     # Engine started

# ------------------------------------------------------------------------------
# Multiple Inheritance
class CombustionEngine():  
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity


class ElectricEngine():  
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

# Child class inherited from CombustionEngine and ElectricEngine
class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)

car = HybridEngine()
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.printDetails()

# ------------------------------------------------------------------------------
# Hybrid Inheritance
class Engine:  # Parent class
    def setPower(self, power):
        self.power = power


class CombustionEngine(Engine):  # Child class inherited from Engine
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity


class ElectricEngine(Engine):  # Child class inherited from Engine
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

# Child class inherited from CombustionEngine and ElectricEngine


class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print("Power:", self.power)
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)


car = HybridEngine()
car.setPower("2000 CC")
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.printDetails()

# ------------------------------------------------------------------------------
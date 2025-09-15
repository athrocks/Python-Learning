# List
num_seq = range(1, 11)
print(num_seq)

num_list = list(num_seq)
print(num_list)

world_cup_winners = [[2006, "Italy"], [2010, "Spain"], [2014, "Germany"], [2018, "France"]]
print(world_cup_winners)

print(world_cup_winners[2])  # Accessing the third element
print(world_cup_winners[2][1])  # Accessing the second element of the third element

part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
merged_list = part_A + part_B
print(merged_list)

# extend keyword
part_A.extend(part_B)
print(part_A)

# common list operations
# Adding Elements
num_list = [] # empty list
num_list.append(1)
num_list.append(2)
num_list.append(3)
print(num_list)

num_list.insert(1, 4)  # insert 4 at index 1
print(num_list)

# Removing elements
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
last_house = houses.pop()
print(last_house)
print(houses)

houses.remove("Hufflepuff")
print(houses)

num_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(num_list[2:5])
print(num_list[0::2])

# Retrieve element position in List
cities = ["London", "Paris", "Los Angeles", "Beirut"]
print(cities.index("Los Angeles"))

cities = ["London", "Paris", "Los Angeles", "Beirut"]
print("London" in cities)
print("Moscow" not in cities)

# Sorting a List
num_list = [20, 40, 10, 50.4, 30, 100, 5]
num_list.sort()
print(num_list)

# Creating a list comprehension
squares = [n**2 for n in num_list]
print(squares)

# Tuples
# Tuples are immutable sequences
dimensions = (1920, 1080, 32)
print(dimensions[0])

# Dictionaries
# Dictionaries are key-value pairs
student = {
    "name": "John Doe",
    "age": 21,
    "courses": ["Math", "CompSci"]
}

print(student["name"])
print(student.get("age"))
student["age"] = 22

# Alternative approach
# dict constructor
empty_dict = dict()
print(empty_dict)

phone_book = dict(Batman=468426, Cersei=237734, Ghostbusters=44678)
print(phone_book)

phone_book2 = dict([('Batman', 468426),
                   ('Cersei', 237734),
                   ('Ghostbusters', 44678)])
print(phone_book2)

# Set
# A set is an unordered collection of unique elements


random_set = {"Educative", 1408, 3.142,
              (True, False)}
print(random_set)
print(len(random_set))  

random_set = set({"Educative", 1408, 3.142, (True, False)})
print(random_set)

# type operator
test_set = {"Educative", 1408, 3.142, (True, False)}
test_lst = ["Educative", 1408, 3.142, (True, False)]
test_dic = {1: "Educative", 2: 1408, 3: 3.142, 4: (True, False)}
test_tup = ("Educative", 1408, 3.142, (True, False))

print(type(test_set))  
print(type(test_lst))  
print(type(test_dic))  
print(type(test_tup))  
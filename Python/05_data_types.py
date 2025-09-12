isRaining = True
isSunny = False

print("Is it raining?:", isRaining)
print("Is it sunny?:", isSunny)

# Escape characters
str_1 = "Hello\'World'"
print(str_1)

str_2 = "Hello\nWorld"
print(str_2)

str_3 = "Hello\tWorld"
print(str_3)

# Length of string
random_str = "I am Atharva"
print("Length of string:", len(random_str))

# Accesing characters in a string
message = "Hello, World!"
first = message[0]
print("First character:", first)
last = message[-1]
print("Last character:", last)

# Strings are immutable
message[0] = 'h'  # This will raise an error
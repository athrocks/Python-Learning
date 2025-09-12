light = input('Enter the traffic light color (Green, Yellow, Red): ')

if light == 'Green':
    print('Go')

elif light == 'Yellow':
    print('Get Ready')

elif light == 'Red':
    print('Stop')

else:
    print('Incorrect light color')

# Floating point number comparison
num1 = 0.1 + 0.2
num2 = 0.3
if num1 == num2:
    print("Equal")
else:
    print("Not Equal")

# Tolerance Value
import math

print(math.isclose(num1, num2))  # True
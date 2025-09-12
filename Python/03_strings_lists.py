String1 = "Educative"
print(String1)

print(String1[0], '=', String1[-9])  # Displaying first element of string
print(String1[8], '=', String1[-1]) # Displaying tenth element of string

print(String1[0:4])  # Displaying first four elements of string
print(String1[3:-3])  # Displaying elements from index 3 to index -3
print(String1[:])  # Displaying all elements of string

msg = '''This string has text1 
and text2 in it
and is multiline string'''
print(msg)

String2 = String1 + ' Learner'
print(String2)

listOfFruits = ["apple","mango","banana"] # Creating a list of strings
print(listOfFruits)

list3 = [50, 'Learn', 10, 'To', 2.5, -1, 'Code']
print("\nList with the use of mixed values: ")
print(list3)

letters = ['a','b','c','d','e','f','g','h','i']
print("List of letters: ")
print(letters)

print('Slice "[1:]" from index 1 till the end')
print(letters[1:])
print('Slice "[-2:]" from index -2 till the end')
print(letters[-2:])
 
print('Slice "[:3]" from start of the list till before index 3')
print(letters[:3])

vals = [-5, 'Python', 3.8]
for v in vals:
   print (v)

mix = ['a',1,2.5,'i',50,6,'m',4.4,6.7,'s','@educative']
print('\nList index using "len()" in range()')
for v in range(len(mix)):
   print (mix[v])


# Fibonacci series using list
n = int(input("Enter number of elements (max 20): "))
if (n > 20) or (n <= 0):
    print("Please enter a valid number")
else:
   fib = [0]*n
   print("Fibonacci series:", fib)
   if n == 1:
       fib[0] = 0
   if n >= 2:
       fib[1] = 1
   for i in range(2,n):
        fib[i] = fib[i-1] + fib[i-2]
   print("Fibonacci series:", fib)


alist = ['aa', ['b', 'c'], 'dd'] # Creating a nested list
print(alist)

matrixA = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] # Creating a matrix
print("Matrix:",matrixA)

rows,cols = 3,4
for i in range(rows): # Outer loop for rows
   for j in range(cols): # Inner loop for columns
        print(matrixA[i][j], end = " ")
   print()
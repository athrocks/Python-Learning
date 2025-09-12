for a in [0, 1, 2, 3, 4]:
    print(a)

for a in range (0,101,5):
    print(a)

a = int(input("Enter a number: "))
while a > 0:
    print(a % 10)
    a //= 10
    print("a is:",a)
print()

for e in ['a','b','c']:
    for m in [1,2,3]:
        print(e,m)
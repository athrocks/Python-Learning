# Operators
# Logical Operators: and, or, not
# Compound Logical Assignment Operators: &=, |=
x = True
y = False
x &= y  # x = x and y
print(x)  # False

z = True
z |= y  # z = z or y
print(z)  # True

# Bitwise Operators: &, |, ^, ~, <<, >>
# Bit Manipulation

print(bin(5))  # 0b101   ->   0101
print(bin(3))  # 0b011   ->   0011

print(5 & 3)   # 1 (0b001) -> 0001 -> 1 in decimal

print(5 | 3)   # 7 (0b111) -> 0111 -> 7 in decimal

print(5 ^ 3)   # 6 (0b110) -> 0110 -> 6 in decimal

print(~5)      # -6 (two's complement)  ~5(0101) -> (1010) -> -6 in decimal

print(5 << 1) # 10 (0b1010) -> 1010 -> 10 in decimal => 5(0101) shifted left by 1 -> 01010 in python left 0 does not matter => 1010
print(bin(5 << 2)) # 20 (0b10100) -> 10100 -> 20 in decimal => 5(0101) shifted left by 2 -> 10100 => 0101 -> 01010 -> 010100 => 10100

print(5 >> 1) # 2 (0b10) -> 10 -> 2 in decimal => 5(0101) shifted right by 1 -> 0010 in python left 0 does not matter => 10 => 2 in decimal
print(bin(5 >> 1)) # 0b10


# Num even or odd
# method 1
num = 6

lsd = bin(num)[-1]
if(int(lsd) == 0):
    print(0)
else:
    print(1)


# method 2
print(num & 1)
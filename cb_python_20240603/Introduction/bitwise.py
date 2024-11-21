# Bitwise AND (`&`)

a = 12  # Binary 1100 
b = 5   # Binary 0101

result = a & b # Binary: 0100, Decimal: 4

print(f"Bitwise AND: {a} & {b} = {result}")

# 2. Bitwise OR (|)
# Performs a bitwise OR operation between two numbers.
result = a | b  # Binary: 1101, Decimal: 13

print(f"Bitwise OR: {a} | {b} = {result}", bin(a), bin(b), bin(result))

# 3. Bitwise XOR (^)
# Performs a bitwise XOR operation between two numbers.
result = a ^ b  # Binary: 1001, Decimal: 9
print(f"Bitwise XOR: {a} ^ {b} = {result}")

# 4. Bitwise NOT (~)
# Performs a bitwise NOT operation on a number.
result = ~a  # Binary: -1101, Decimal: -13 (two's complement)
print(f"Bitwise NOT: ~{a} = {result}")

# 5. Bitwise Left Shift (<<)
# Shifts the bits of the number to the left by the specified number of positions.
result = a << 2  # Binary: 110000, Decimal: 48
print(f"Bitwise Left Shift: {a} << 2 = {result}")

# 6. Bitwise Right Shift (>>)
# Shifts the bits of the number to the right by the specified number of positions.

result = a >> 2  # Binary: 0011, Decimal: 3
print(f"Bitwise Right Shift: {a} >> 2 = {result}")
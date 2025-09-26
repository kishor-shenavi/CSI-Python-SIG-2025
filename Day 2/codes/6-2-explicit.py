# Numeric Conversions Example

x = 12.7
y = int(x)          # float → int
z = float(y)        # int → float
c1 = complex(y)     # int → complex
c2 = complex(y, 3)  # int → complex with imaginary part

print("Original value:", x, type(x))
print("int(x):", y, type(y))
print("float(y):", z, type(z))
print("complex(y):", c1, type(c1))
print("complex(y,3):", c2, type(c2))



# String Conversions Example

num = 25
f = 12.5
b = True

str_num = str(num)   # int → str
str_f = str(f)       # float → str
str_b = str(b)       # bool → str

print("Original values and types:")
print(num, type(num))
print(f, type(f))
print(b, type(b))

print("\nAfter converting to string:")
print(str_num, type(str_num))
print(str_f, type(str_f))
print(str_b, type(str_b))

# Example use: concatenation
name = "Alice"
age = 21
print("\nHello " + name + ", your age is " + str(age))

# Collection Conversions Example

# Original collections
tup = (1, 2, 3, 2)      # tuple
lst = [4, 5, 5, 6]      # list
l = [1, 2, 2, 3, 3]     # list with duplicates

# Conversions
list_from_tuple = list(tup)   # tuple → list
tuple_from_list = tuple(lst)  # list → tuple
set_from_list = set(l)        # list → set (duplicates removed)

print("Original collections:")
print("Tuple:", tup)
print("List:", lst)
print("List with duplicates:", l)

print("\nAfter conversions:")
print("list(tup):", list_from_tuple)
print("tuple(lst):", tuple_from_list)
print("set(l):", set_from_list)



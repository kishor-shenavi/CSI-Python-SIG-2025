# Numeric Types
a = 10                 # int: Integer
b = 3.14               # float: Floating-point number
c = 2 + 3j             # complex: Complex number
print("Numeric Types:")
print(f"int: {a}, float: {b}, complex: {c}\n")


# # Sequence Types
d = "Hello, World!"    # str: String
e = [1, 2, 3]          # list: Mutable ordered collection
my_list = [1, "hello", 3.14, True]
f = (4, 5, 6)          # tuple: Immutable ordered collection
# my_tuple[0] = 100   ❌ Error: 'tuple' object does not support item assignment
# my_tuple.append(4)  ❌ Error: 'tuple' object has no attribute 'append'

print("Sequence Types:")
print(f"str: {d}, list: {e}, tuple: {f}, tuple: {my_list}\n")

# Mapping Type
# dict: Key-value pairs
my_dict = {
    "name": "Alice",
    "age": 30,
    "is_active": True
}
print(my_dict["name"])

# Boolean Type
k = True               # bool: True or False
print(f"bool: {k}\n")

# Set Types
h = {7, 8, 9, 7, 10}          # set: Mutable collection of unique items
i = frozenset({10, 11, 12})  # frozenset: Immutable version of set
print(f"set: {h}, frozenset: {i}\n")

s = {1, 2, 3, 2, 1}
print(s)  # Output: {1, 2, 3} — duplicates removed
s.add(4)       # Add an element
s.remove(2)    # Remove an element (raises error if not found)
s.discard(10)  # Removes safely (no error if not found)

# None Type
l = None               # NoneType: Represents the absence of a value
print(f"NoneType: {l}\n")


x = 42       # Integer
y = 3.14     # Float
z = [1, 2, 3] # List

print(type(x), type(y), type(z))
# to check data types in python you can use type() function
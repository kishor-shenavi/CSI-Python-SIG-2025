# Creating Tuples

# Empty tuple
t = ()


# Single element tuple (needs comma!)
t1 = (5,)
print(t1)

print(type(t1))



# Multiple elements
t2 = (1, 2, 3, 4)

# # Mixed types
t3 = (1, "apple", 3.14, True)



# Accessing Tuple Elements
# Use indexing and slicing like lists.
fruits = ("apple", "banana", "cherry", "date")

print(fruits[0])      
print(fruits[-1])     
print(fruits[1:3]) # 1, 2     
print(fruits[::3])     


# Tuple Operations

t1 = (1, 2, 3)
t2 = (4, 5)

# Concatenation
t3 = t1 + t2
print(t3)   # (1, 2, 3, 4, 5)

# Repetition
t4 = t1 * 2
print(t4)   # (1, 2, 3, 1, 2, 3)

# Membership
print(5 in t1)    # True


#Tuple Methods
#Tuples have only two main methods:

t = (1, 2, 2, 3, 4, 2, 3)

print(t.count(2))   # 3 → counts occurrences
print(t.index(3))   # 3 → first index of 3



# Tuple Packing and Unpacking

#Packing: Storing multiple values in a single tuple.
#Unpacking: Assigning tuple elements to variables.

# Packing
person = ("kishor", 20, "CS")
#Unpacking
name, age, department = person
print(name, age, department)  # kishor 20 CS



# Nested Tuples
# Tuples can contain other tuples or lists.
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(matrix[2][1])   




# Converting Between Lists and Tuples
# List → Tuple
lst = [1, 2, 3]
t = tuple(lst) # int()
print(t)

# Tuple → List
t2 = (4, 5, 6)
lst2 = list(t2)
print(lst2)



# Iterating Through Tuples

# For loop:
fruits = ("apple", "banana", "cherry")
for f in fruits:
    print(f)


# While loop:
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1



# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
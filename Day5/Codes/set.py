# Using curly braces
myset = {1, 2, "apple", 4, 5} 
print(myset)
# Using set() function
myset2 = set([1, 2, 2, 3, 4])
print(myset2)   

# Empty set
empty_set={}
print(type(empty_set))   # {} is dictionary, not set

empty = set()   
print(type(empty))


# Adding Elements

# add() → add a single element
# update() → add multiple elements (list, set, tuple)
s = {1, 2, 3}
s.add(4)           # {1, 2, 3, 4}
print(s)
s.update([7,4,10, 5,5,6])   # {1, 2, 3, 4, 5, 6}
print(s)


# Removing Elements

# remove(element) → raises error if not present
# discard(element) → does not raise error
# pop() → removes random element
# clear() → removes all elements

s = {1, 2, 3, 4}
s.remove(3)   # {1, 2, 4}
print(s)
s.discard(10) # no error
print(s)
x = s.pop()   # removes a random element
print(s)
s.clear()     # {}
print(s)


#  Set Operations

# Union (| or union()) → combines sets
# Intersection (& or intersection()) → common elements
# Difference (- or difference()) → elements in first not in second
# Symmetric Difference (^ or symmetric_difference()) → elements in either set, not both

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Using |
print(A | B)          
# Using union()
print(A.union(B))    


# Using &
print(A & B)          
# Using intersection()
print(A.intersection(B))   


# Using -
print(A - B)        
# Using difference()
print(A.difference(B))  
print(B - A)        
# Using difference()
print(B.difference(A))  


# Using ^
print(A ^ B)          # {1, 2, 5, 6}
# Using symmetric_difference()
print(A.symmetric_difference(B))  # {1, 2, 5, 6}


# Set Membership
s = {1, 2, 3}
print(2 in s)   # True
print(5 not in s) # True


# Iterating Through a Set
s = {"apple", "banana", "cherry"}
for item in s:
    print(item)         # Note: Order is not guaranteed.


#Frozen Set 
#Immutable Set ,  i.e cannot modify
fs = frozenset([1, 2, 3])
print(fs)
fs.add(4) # → Error
fs.remove(1)



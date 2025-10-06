# Key → unique identifier
# Value → data associated with the key

# Creating Dictionaries
# Using curly braces
d1 = {"name": "Alice", "age": 21}

# Using dict() function
d2 = dict(name="Bob", age=22, branch="IT")

# Empty dictionary
d3 = {}


# Accessing Dictionary Items
student = {"name": "Kishor", "age": 20, "branch": "CS"}

# Access using key
print(student["name"])  

# Using get() method
print(student.get("age"))   
print(student.get("branch","not found"))  # Not Found



# Adding & Updating Items
student = {"name": "Kishor", "age": 20}
print(student)

# Adding a new key-value pair
student["branch"] = "IT"

# Updating an existing key
student["age"] = 22

print(student)  # {'name': 'Alice', 'age': 22, 'branch': 'CS'}


# Removing Items
student = {"name": "Kishor", "age": 20, "branch": "CS"}

# Remove a key
student.pop("age")  
print(student)

# Remove last inserted item
student.popitem() 
print(student) 

# Delete a key
del student["branch"]

# Clear dictionary
student.clear()  




# Iterating Through Dictionaries
student = {"name": "Kishor", "age": 20, "branch": "CS"}

# Iterating keys
for key in student:
    print(key)

# Iterating values
for value in student.values():
    print(value)

# Iterating key-value pairs
for key, value in student.items():
    print(key, value)


# Dictionary Methods
# Method	Description
# keys()	Returns all keys
# values()	Returns all values
# items()	Returns key-value pairs as tuples
# get(key, default)	Returns value or default if key not found
# update()	Updates dictionary with another dictionary
# pop(key)	Removes key and returns value
# popitem()	Removes last inserted key-value pair
# clear()	Clears all items

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1.update(d2)
print(d1)  


# Nested Dictionaries
students = {
    1: {"name": "Kishor", "age": 20},
    2: {"name": "Prasad", "age": 21}
}

print(students[2]["name"])  

#Only stop

for i in range(5): 
    print(i)

#Start and stop
for i in range(1, 6):  
    print(i)

#Start, stop, and step

for i in range(2, 11, 2):  
    print(i)

# Negative step (counting backward)
for i in range(5, 0, -1):  
    print(i)

# Loop through a list
fruits = ["Apple", "Banana", "Mango"]
for fruit in fruits:
    print(fruit)

# Loop through a string
for letter in "HELLO":
    print(letter)

#task 
# Ask the user for a number
n = int(input("Enter a number: "))

# Loop from 1 to n
for i in range(1, n + 1):
    print(i)


# Nested loop
for i in range(1, 4):      # Outer loop
    for j in range(1, 4):  # Inner loop
        print(i, j)


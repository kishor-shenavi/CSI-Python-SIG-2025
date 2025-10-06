fruits = ["apple", "banana", "cherry"]
print(fruits)             # ['apple', 'banana', 'cherry']
print(type(fruits))       # <class 'list'>


# Indexing and Slicing
# Positive indexing starts from 0.
# Negative indexing starts from -1.


nums = [10, 20, 30, 40, 50]
print(nums[0])       # 10
print(nums[-1])      # 50
print(nums[1:7])     # [20, 30, 40] (start:stop)
print(nums[:3])      # [10, 20, 30]
print(nums[1:])      
print(nums[::3])    
print(nums[:]) 


# Adding Elements

# append() → adds at end
# insert(index, value) → adds at position
# extend() → add multiple values


nums = [1, 2, 3]
nums.append(4) #[1, 2, 3, 4]
print(nums)
nums.insert(1, 10) #[1, 10, 2, 3, 4]
print(nums)
nums.extend([5])
print(nums)   # [1, 10, 2, 3, 4, 5, 6]


#Exercise: Start with an empty list. Take 5 user inputs and store them in the list.
nums=[1, 2, 3]
for i in range(5):
    a=int(input(f"enter number {i+1}:"))
    nums.extend([a])

# print("the list is ",num)
nums[2]= 4
print(nums)


# . Removing Elements

# remove(value) → removes first match
# pop(index) → removes at index (default last)
# clear() → removes all elements

nums = [10, 20, 30, 40, 50, 30]
nums.remove(30)      # removes 30 [10, 20, 40, 50]

nums.remove(20)
print(nums)

nums.pop(0)          # removes element at index 2
print(nums)
nums.clear()         # []

# Exercise: Make a list of fruits, remove the second fruit, and then clear the entire list.



# Updating Values
# Lists are mutable → you can change elements.

nums = [1, 2, 3]
nums[1] = 20
nums[0] = 10
print(nums)   # [1, 20, 3]


#Useful List Methods
nums = [1, 5, 7, 2, 8, 3]
# print(nums.count(2))       # 2 (frequency)
# print(nums.index(2))       # 3 (position)
nums.reverse()             # [5, 4, 3, 2, 2, 1]
print(nums)
nums.sort()                # [1, 2, 2, 3, 4, 5]
print(nums)
print(sorted(nums, reverse=True))  # [5, 4, 3, 2, 2, 1]
nums.sort(reverse=True)
print(nums)



# Copying Lists

# Direct assignment links lists → changes affect both.
# Use copy() or slicing for a new list.

a = [1, 2, 3]
b = a
c = a.copy()
a.append(4)
print(b)   # [1, 2, 3, 4]
print(c)   # [1, 2, 3]



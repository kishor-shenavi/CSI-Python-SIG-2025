# def show():
#     print("Welcome to PCSB!!")
    
# show()

# def display():
#     x = 2
#     y = 5
#     print(f"the value of x is: {x}")
#     print(f"the value of y is: {y}")
    
# display()

# def add(x, y):
#     res = x + y
#     print(res)
    
# x = int(input("enter first number:"))
# y = int(input("enter second number:")) 
# add(x, y)

# import math
# def isPrime(num):
#     i = 2
#     isprime = True
#     while i <= math.sqrt(num):
#         if num % i == 0:
#             isprime = False
#             break
#         i += 1
#     if isprime:
#         print(num, "is prime.")
#     else:
#         print(num, "is not prime.")

# isPrime(5)

# def display(name = "world"):
#     print(f"Hello {name}!!")

# #
# display("John")

# def multiply(a, b =5):
#     res = a * b
#     print(res)
    
# # multiply(7)
# multiply(10, 4)


# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old!")

# greet(age=21, name="Pushkar")


# def nameAge(name, age):
#     print("Hi, I am", name)
#     print("My age is ", age)

# # nameAge("Pushkar", 21)
# nameAge(21, "Pushkar")


# def add_numbers(*args):
#     print(type(args))
#     total = 0
#     for num in args:
#         total += num
#     print("Sum:", total)

# #add_numbers(2, 3)          
# add_numbers(1, 2, 3, 4, 5) 


# def show(*args, **kwargs):
#     print("Positional:", args)
#     print("Keyword:", kwargs)

# show(1, 2, 3, name="Pushkar", age=21)


# def cube(a):
#     return a ** 3

# x = 5
# result = cube(x)
# print(f"Cube of {x} is: {result}")


# def check_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# number = 7
# if check_even(number):
#     print(number, "is even")
# else:
#     print(number, "is odd")


# def arithmetic_operations(a, b):
#     add = a + b
#     sub = a - b
#     multiply = a * b
#     divide = a / b
#     return add, sub, multiply, divide

# sum, diff, prod, div = arithmetic_operations(10, 5)
# print("Sum:", sum)
# print("Difference:", diff)
# print("Product:", prod)
# print("Division:", div)


# def my_function():
#     x = 10
#     print("the value of x is", x)

# my_function()
# print(x)

# y = 20
# def show():
#     print("Inside function, y =", y)

# show()
# print("Outside function, y =", y)

count = 0
def increment():
    global count
    count += 1
    print("Inside function, count =", count)

increment()
#increment()
print("Outside function, count =", count)


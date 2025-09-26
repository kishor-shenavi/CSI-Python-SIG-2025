# Python SIG CSI – Day 1 Assignments Answer Sheet

### **1. Variables & Data Types**
```python
a = 10          # Integer
b = 20.5        # Float
c = "Hello"     # String
d = True        # Boolean

print("a =", a, "Type:", type(a))
print("b =", b, "Type:", type(b))
print("c =", c, "Type:", type(c))
print("d =", d, "Type:", type(d))
````

*Assign values to different data types and use `type()` to check the data type.*



### **2. Input/Output – Greeting User**

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}! You are {age} years old.")
```

*Take user input using `input()` and display a formatted message using f-strings.*

---

### **3. Arithmetic Operations**

```python
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus:", x % y)
```

*Perform basic arithmetic operations using `+`, `-`, `*`, `/`, `%`.*

---

### **4. Logical Operators**

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Are both numbers greater than 50?", num1 > 50 and num2 > 50)
```

*Use logical operator `and` to check multiple conditions.*

---

### **5. Positive, Negative, or Zero**

```python
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

*Use `if-elif-else` to check whether a number is positive, negative, or zero.*

---

### **6. Largest Among Three Numbers**

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("The largest number is:", a)
elif b >= a and b >= c:
    print("The largest number is:", b)
else:
    print("The largest number is:", c)
```

*Compare all three numbers using `if-elif-else` to find the maximum.*

---

### **7. Leap Year Check**

```python
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
```

*Leap years are divisible by 400, or divisible by 4 but not by 100.*

---

### **8. Even or Odd**

```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")
```

*A number is even if divisible by 2, otherwise odd.*

---

### **9. Student Grading System**

```python
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
```

*Grades are assigned using conditional ranges.*

---

### **10. Divisibility by 3 and/or 5**

```python
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print(num, "is divisible by both 3 and 5")
elif num % 3 == 0:
    print(num, "is divisible by 3 only")
elif num % 5 == 0:
    print(num, "is divisible by 5 only")
else:
    print(num, "is not divisible by 3 or 5")
```

*Use `and`, `elif`, and modulus operator to check divisibility cases.*

---



## 📧 Contact

For questions, reach out to **CSI PICT Core Team**.
Happy Learning! 🚀


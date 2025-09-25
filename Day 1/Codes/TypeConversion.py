# Implicit conversion from int to float
num_int = 5
num_float = num_int + 2.5
print(num_float)  # Output: 7.5
print(type(num_float))  # Output: <class 'float'>


# Explicit conversion using built-in functions from int to str
value = 123
string_value = str(value)
print(string_value)  # Output: "123"
print(type(string_value))  # Output: <class 'str'>


value = "42"
int_value = int(value)
print(int_value)  # Output: 42
print(type(int_value))  # Output: <class 'int'>


# Type Conversion (Casting) Examples
# Integer to Float
int_value = 10
float_value = float(int_value)  # Convert int to float
print(f"Integer to Float: {int_value} -> {float_value}")

# Float to Integer
float_value = 12.56
int_value = int(float_value)  # Convert float to int (truncates the decimal part)
print(f"Float to Integer: {float_value} -> {int_value}")

# Integer to String
int_value = 42
str_value = str(int_value)  # Convert int to string
print(f"Integer to String: {int_value} -> '{str_value}'")

# String to Integer
str_value = "123"
int_value = int(str_value)  # Convert string to int (only works for numeric strings)
print(f"String to Integer: '{str_value}' -> {int_value}")

# String to Float
str_value = "45.67"
float_value = float(str_value)  # Convert string to float
print(f"String to Float: '{str_value}' -> {float_value}")

# Float to String
float_value = 78.9
str_value = str(float_value)  # Convert float to string
print(f"Float to String: {float_value} -> '{str_value}'")

# String to Boolean
str_value = "True"
bool_value = bool(str_value)  # Convert string to boolean (non-empty string becomes True)
print(f"String to Boolean: '{str_value}' -> {bool_value}")

# Integer to Boolean
int_value = 0
bool_value = bool(int_value)  # Convert int to boolean (0 is False, non-zero is True)
print(f"Integer to Boolean: {int_value} -> {bool_value}")

# Boolean to Integer
bool_value = True
int_value = int(bool_value)  # Convert boolean to integer (True is 1, False is 0)
print(f"Boolean to Integer: {bool_value} -> {int_value}")



x = 1         +         2
+ 3  # Python thinks this is a separate statement.
print(x)  # Output: 3

# the backslash \ tells Python to continue the expression on the next line.
x = 1 + 2 \
+ 3
print(x)  # Output: 6

x = (
    1 + 2
    + 3
)
print(x)  # Output: 6

# Whitespace does matter inside strings or variable names.

# name = "Prajwal"
# print(name)        # ✅ Works
# na me = "Error"    # ❌ Invalid Syntax

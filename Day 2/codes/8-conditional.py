#if 
age = 20
if age >= 18:
    print("You are an adult")


#if-else
age = 15
if age >= 18:
    print("Adult")
else:
    print("Minor")

#if-elif-else - order matters, only first true condition is executed

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")



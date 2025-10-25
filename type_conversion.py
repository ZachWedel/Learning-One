x = input("x: ")
print(type(x))  # Output: <class 'str'>
y = int(x) + 1
print(f"x: {x}, y: {y}")

int(x)  # Type conversion from string to integer
float(x)  # Type conversion from string to float
bool(x)  # Type conversion from string to boolean
str(x)  # Type conversion from string to string

# Falsy values: "", 0, 0.0, None, [], {}, set(), False

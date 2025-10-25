import math

print(round(2.9))  # Rounds to nearest integer
print(abs(-2.9))   # Absolute value

math.ceil(2.2)  # Rounds up to nearest integer
math.floor(2.9)  # Rounds down to nearest integer
math.sqrt(16)   # Square root
math.pow(3, 2)  # 3 raised to the power of 2
math.log10(100)  # Base-10 logarithm
math.sin(math.pi / 2)  # Sine of 90 degrees
math.cos(0)      # Cosine of 0 degrees
math.tan(math.pi / 4)  # Tangent of 45 degrees
math.factorial(5)  # Factorial of 5
x = 10
y = math.sqrt(x)
z = math.pow(x, 3)
result = round(y) + z
print(result)

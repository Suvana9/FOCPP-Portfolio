# Syntax error example (DO NOT RUN – for learning only)
# 10 +

# Runtime error example (handled safely)
try:
    print("Ten divided by zero is", 10 / 0)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
Python Programming Exercises (Weeks 1–8)

This repository contains completed weekly exercise logbooks for a Python programming module.
It covers core Python concepts including variables, functions, data structures, scripts, modules, and file handling.

Each week is organized with exercises and example Python code.

-----------------------------------------
Week 1 – Introduction to Python

Topics Covered:
- Introduction to programming
- What is Python?
- Using the Python interpreter
- Writing and running basic Python programs
- Printing output to the screen

Notes:
Week 1 focused on understanding the Python environment, running simple commands, and becoming familiar with basic syntax such as print() and comments.

-----------------------------------------
Week 2 – Variables and Types

Topics Covered:
- Variables and assignment
- Data types (int, float, str, bool)
- Dynamic typing
- Strings and indexing
- Lists and mutability
- Input and output

Examples:

pi = 3.142

print("The age value is", 35)

print('Hello, is your name "Bwian"?')
print("Or is your name 'Woger'?")

print("This is a string containing a backslash (\\),\n a single quote ('), a double quote (\") \n and is split across multiple lines")

print("""This is a string containing a backslash (\),
 a single quote ('), a double quote (")
 and is split across multiple lines""")

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print("Temperature in Celsius:", celsius)

a = float(input("Enter value a: "))
b = float(input("Enter value b: "))

print("The value 'a' was", a, "and the value 'b' was", b)
print("The sum of 'a' and 'b' is", a + b)
print("The product of 'a' and 'b' is", a * b)

num1 = float(input("Enter first value: "))
num2 = float(input("Enter second value: "))
num3 = float(input("Enter third value: "))
print("The largest value is:", max(num1, num2, num3))

name = "Black Knight"
print(name[0])
print(name[4])
print(name[-1])
print(name[2:5])

names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
names[0:1] = ["Mark", "Jon"]
print(names)

len(names)

-----------------------------------------
Week 3 – Control Flow (Selection & Iteration)

Topics Covered:
- Conditional statements (if, elif, else)
- Comparison and logical operators
- Loops (for, while)
- Using range()
- Basic algorithm logic

Notes:
This week focused on controlling program flow, making decisions, and repeating operations using loops.

-----------------------------------------
Week 4 – Functions

Topics Covered:
- Defining functions
- Parameters and return values
- Default arguments
- Docstrings
- Variable-length arguments
- Lambda functions

Examples:

def print_header(msg):
    print("*****" + msg)

def print_header(msg):
    """
    Displays the given message preceded by five asterisks.
    """
    print("*****" + msg)

def find_min(a, b):
    if a < b:
        return a
    else:
        return b

def shouldContinue(prompt, answer=False):
    pass

cube = lambda x: x ** 3

-----------------------------------------
Week 5 – Scripts and Modules

Topics Covered:
- Python scripts
- Command-line arguments
- sys module
- Import statements and aliases
- __name__ variable

Examples:

import sys

for item in sys.argv:
    print(item)

import sys

if len(sys.argv) > 1:
    for name in sys.argv[1:]:
        print(name)
else:
    print("no names provided")

import sys as my_system
from math import floor as lower

-----------------------------------------
Week 6 – Lists and Tuples

Topics Covered:
- List methods
- Mutators vs accessors
- List comprehensions
- Tuples and immutability
- Unpacking sequences

Examples:

prices = [2.65, 7.65, 8.25, 9.56]
prices.append(4.99)
prices.extend([3.45, 6.80, 10.25])

values = [x * x for x in range(100, 200) if x % 2 == 0]

coord = (100, 200, 150)
x, y, z = coord

-----------------------------------------
Week 7 – Sets and Dictionaries

Topics Covered:
- Sets and frozensets
- Set operations
- Dictionaries
- Key-value pairs
- Comprehensions
- Unpacking with **

Examples:

languages = set(["C++", "Java", "C#", "PHP", "JavaScript"])
languages = languages.union({"Python"})

stock = {"apple": 10, "banana": 15, "orange": 11}
print(stock["banana"])

lang_gen = dict([("Java", 3), ("Assembly", 2), ("Machine Code", 1)])

-----------------------------------------
Week 8 – I/O and File Handling

Topics Covered:
- f-strings and formatting
- Reading and writing files
- File modes
- File cursor control
- with statement

Examples:

value = 10.768572
print(f"Value is {value:.2f}")

for n in range(10, 0, -1):
    print(("#" * n).rjust(10))

with open("data.txt", "w") as f:
    f.write("Hello Python")

with open("data.txt", "r") as f:
    for line in f:
        print(line)

-----------------------------------------
Notes:
- Compatible with GitHub
- Clean structure
- All weeks included
- Python code examples provided

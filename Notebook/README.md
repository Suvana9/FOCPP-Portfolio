# Introduction to Programming – Lab Worksheets (Weeks 1–8)

## Description
This repository contains all lab worksheets for the Introduction to Programming module. The labs are organized by week and cover fundamental Python programming concepts. Each week includes tasks that demonstrate key programming techniques and concepts, and all tasks are implemented in Python.

## Requirements
- Python 3.8+ recommended
- VS Code (or any Python IDE)

## How It Works
1.Each week is organized into its own folder (Week1, Week2, … Week8).
2.Each task is a separate Python file (.py) that can be run independently.
3.You can open the project in VS Code, open a terminal, navigate to the desired week folder, and run the Python files using:
python task_name.py

# Weekly breakdown

## Week 1 – Basics
### Focus
Python syntax, interpreter, printing output, receiving user input.
### Purpose
Introduces writing Python programs, displaying messages, and performing basic arithmetic.
### Input / Output
- **Input:** User may enter their name, numbers, or text depending on the task.
- **Output:** Program prints messages or calculation results to the console.
### Input Validation
- Use `input()` to accept values.
- Ensure numeric input is converted using `int()` or `float()` where required.
- Handle invalid input using basic checks (optional for Week 1).
### Tasks
Week1 tasks.py files are named as error.py,expression.py,input.py,parentheses.py,precedence.py and printing.py. It prints a simple message, perform basic calculations and accept input and display output.
### Example Input/Output
Enter your name: Jennie
Enter your age: 19
Output: Hello Jennie, you are 19 years old.

## Week 2 - Variables and Data Types
### Focus
It focuses on Variables, numbers, strings, Booleans, type conversion.
### Purpose
It Store, manipulate, and display data.
### Input / Output
Input: User may enter numbers or strings.
Output: Display results or concatenated strings.
### Input Validation
Ensure numeric values are converted using int() or float().
Strings should be handled as-is.
### Tasks 
Week2 tasks work with numbers and strings and it also Convert types and perform calculations.
Shows how to store and manipulate data.
### Example Input/Output
Enter a number: 5
Output: Number squared: 25

## Week 3 - Conditionals
### Focus
if, elif, else statements, Boolean logic, ternary expressions.
### Purpose
Control the flow of programs based on conditions.
### Input / Output
Input: User enters numbers or text for comparison.
Output: Program prints decisions or messages.
### Input Validation
Ensure numeric input is properly converted.
Handle unexpected text input gracefully (optional).
### Tasks
Control program flow based on conditions.
### Example Input / Output:
Enter your age: 18
Output: You are an adult.

## Week 4 - Loops
### Focus
for loops, while loops, break, continue.
### Purpose
Repeat tasks efficiently and automate processes.
### Input / Output
Input: Loop counts or data from the user.
Output: Repeated messages, calculations, or patterns.
### Input Validation
Ensure loop counts are numeric.
Handle empty or invalid input.
### Tasks
The tasks repeat actions efficiently.
### Example Input / Output:
Enter a number to count down from: 3
Output:
3
2
1
0

## Week 5 - Functions
### Focus
Defining functions, parameters, return values, scope.
### Purpose
Write reusable code and improve organization.
### Input / Output
Input: Values passed to functions.
Output: Return values or printed results.
### Input Validation
Ensure numeric input is converted correctly.
Check for valid function arguments.
### Tasks
Demonstrates reusable code blocks.
### Example Input / Output:
Enter width: 5
Enter height: 3
Output: Area of rectangle: 15

## Week 6 - Lists and Tuples
### Focus
Lists and tuples: storing multiple values, accessing elements.
### Purpose
Manage collections of data efficiently.
### Input / Output
Input: Values to store in lists or tuples.
Output: Display selected elements or results.
### Input Validation
Ensure numeric input is converted if needed.
Handle empty lists/tuples.
### Tasks
Efficiently manage multiple values.
### Example Input / Output:
List: [1, 2, 3]
After append: [1, 2, 3, 4]

## Week 7 -Sets and Dictionaries
### Focus
Set operations, dictionaries (key-value pairs).
### Purpose
Store unique values and map keys to values.
### Input / Output
Input: User may add or lookup values.
Output: Display set contents or dictionary entries.
### Input Validation
Ensure unique inputs for sets.
Ensure valid dictionary keys exist before access.
### Tasks
Demonstrates advanced data structures. 
### Example Input / Output:
Set A: {1, 2, 3}
Set B: {3, 4}
Union: {1, 2, 3, 4}
Intersection: {3}

## Week 8 - Input/Output and File Handling
### Focus
Display output with formatting (f-strings, str.format())
Read/write text files
Append data, random file access, with statement
### Purpose
Learn to interact with users and files, format outputs, and handle exceptions.
### Input / Output
Input: User input for calculations or files.
Output: Formatted console output and file updates.
### Input Validation
Ensure numeric inputs are converted.
Check files exist before reading.
Handle invalid lines gracefully.
### Tasks
Teaches file handling, formatting, and exception handling.

task1_rectangle_area_fstring.py
Description: Format rectangle area using f-strings
Example Output:
The area of a rectangle with width 104.32 and height 15.654 is 1634.961

task2_rectangle_area_3dp.py
Description: Limit area to 3 decimal places
Example Output:
The area of a rectangle is 1634.961

task3_alignment_demo.py
Description: Column width, alignment, fill character
Example Output:
$$$$$$$$$$Donald$$$$$$$$$$ - $$$$$$$75.00$$$$$$$

task4_right_align_fill.py
Description: Advanced alignment formatting

task5_strformat_circle_area.py
Description: Use str.format() to display area
Example Output:
A circle with radius 52 has an area of 8494.8665353068

task6_convert_to_strformat.py
Description: Convert f-string to str.format()

task7_read_full_file.py
Description: Read entire contents of info.txt

task8_read_three_line.py
Description: Read lines individually

task9_for_loop_read.py
Description: Iterate file with for loop

task10_append_line.py
Description: Append text to file

task11_with_statement.py
Description: Use with to auto-close file
### Example Input / Output:
Rectangle width: 104.32
Rectangle height: 15.654
Output: The area of the rectangle is 1634.961

## How to Run Tasks
1.Open the project in VS Code.
2.Open the terminal: View → Terminal.
3.Navigate to the week folder:
cd Week8_IO_FileHandling
4.Run a task:
python task1_rectangle_area_fstring.py

## Key Concepts Covered
1.Python basics: syntax, variables, data types
2.Conditional statements and loops
3.Functions and scope
4.Collections: lists, tuples, sets, dictionaries
5.Input/Output and string formatting
6.File handling and exception handling

## Author
Suvana Gajurel
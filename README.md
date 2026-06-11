DataScience

This repository contains my Python learning and practice files.
The main goal of this project is to improve my understanding of Python fundamentals before moving deeper into data science topics.

Currently, the repository includes small examples related to functions, arguments, lambda expressions, map(), filter(), scope, and basic string operations.

About

This is a personal learning repository where I collect Python practice tasks and examples.

The project is not a full data science project yet. It is the first step toward learning data analysis, automation, and machine learning with Python.

Technologies
Python 3
GitHub
PyCharm or any Python IDE
Topics Practiced
Python basics
Functions
Positional arguments
*args
**kwargs
Lambda functions
map()
filter()
Local and global variables
String length
String indexing
Project Structure
DataScience/
│
├── args_kwargs.py   # Practice with *args and **kwargs
├── lambda.py        # Practice with map() and regular functions
├── lambda1.py       # Practice with map() and string conditions
├── lambda2.py       # Practice with filter()
├── lambda3.py       # Practice with lambda, map() and filter()
├── main.py          # Basic Python script
├── new.py           # Practice with args and kwargs together
├── scope.py         # Practice with local and global scope
└── test.py          # Practice with strings and indexes
File Descriptions
File	Description
args_kwargs.py	Examples of using *args and **kwargs in Python functions
lambda.py	Example of using map() with a regular function
lambda1.py	Practice with map() and checking string values
lambda2.py	Practice with filter()
lambda3.py	Practice with lambda, map() and filter()
main.py	Basic starter Python file
new.py	Combined practice with positional and keyword arguments
scope.py	Example of local and global variable scope
test.py	Practice with string length and indexing
Code Examples
Example of *args
def print_args(*args):
    print(args)

print_args(1, 2, 3)
Example of **kwargs
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(name="Victoria", role="QA")
Example of lambda
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda number: number * 2, numbers))

print(result)
Example of filter()
numbers = [1, 2, 3, 4, 5, 6]

odd_numbers = list(filter(lambda number: number % 2 == 1, numbers))

print(odd_numbers)
How to Run
Download or clone the repository.
Open the project in PyCharm, VS Code, or another Python IDE.
Choose any .py file.
Run the file.

Example command:

python lambda3.py

or:

python3 lambda3.py
Current Status

The repository is currently focused on Python basics.

Future topics may include:

NumPy
Pandas
Working with CSV files
Data cleaning
Data visualization
Statistics basics
Jupyter Notebook
Simple machine learning examples
Purpose

This repository helps me track my learning progress and keep Python practice examples in one place.

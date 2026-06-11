This repository contains my Python practice files created while learning the basics of programming and preparing for further data science topics.

At this stage, the project focuses on core Python concepts such as functions, arguments, lambda expressions, map(), filter(), variable scope, and basic string operations.

About the project

The goal of this repository is to collect small Python examples and practice tasks in one place.

The current files are mostly focused on Python fundamentals. Later, this repository can be expanded with real data science topics such as NumPy, Pandas, data visualization, statistics, and machine learning.

Technologies
Python 3
PyCharm / any Python IDE
GitHub
Topics covered
Functions
Positional arguments
*args
**kwargs
Lambda functions
map()
filter()
Local and global scope
String length
String indexing
Basic Python scripts
Repository structure
DataScience/
│
├── args_kwargs.py   # Practice with *args and **kwargs
├── lambda.py        # Practice with map() and functions
├── lambda1.py       # Practice with map() and string checks
├── lambda2.py       # Practice with filter()
├── lambda3.py       # Practice with lambda, map() and filter()
├── main.py          # Basic Python script
├── new.py           # Practice with args and kwargs together
├── scope.py         # Practice with local and global scope
└── test.py          # Practice with strings and indexes
How to run the files
Clone the repository:
git clone https://github.com/VictoriaRudakova/DataScience.git
Open the project folder:
cd DataScience
Run any Python file:
python args_kwargs.py

Example:

python lambda3.py

If python does not work, use:

python3 lambda3.py
Example topics
*args

Used when a function can receive any number of positional arguments.

def example_args(*args):
    print(args)

example_args(1, 2, 3)
**kwargs

Used when a function can receive any number of named arguments.

def example_kwargs(**kwargs):
    print(kwargs)

example_kwargs(name="Victoria", role="QA")
Lambda function

A short anonymous function.

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda number: number * 2, numbers))

print(result)
filter()

Used to filter values from a list based on a condition.

numbers = [1, 2, 3, 4, 5, 6]

odd_numbers = list(filter(lambda number: number % 2 == 1, numbers))

print(odd_numbers)
Current status

This is a learning repository.
It is currently focused on Python basics and will be improved step by step.

Future improvements

Planned topics to add:

NumPy basics
Pandas basics
Data cleaning examples
Working with CSV files
Data visualization with Matplotlib
Simple statistics examples
Basic machine learning examples
Jupyter Notebook examples

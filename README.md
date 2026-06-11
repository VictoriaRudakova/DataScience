A small Python learning repository with basic examples of Python syntax, functions and functional programming concepts.

This project contains simple practice scripts created while learning Python fundamentals. The examples cover working with functions, *args, **kwargs, lambda, map(), filter(), variable scope and string indexing.

Topics covered
Python functions
Positional arguments
*args
**kwargs
Lambda expressions
map()
filter()
Variable scope
String length and indexing
Basic script execution in Python
Project structure
DataScience/
│
├── args_kwargs.py   # Examples of *args and **kwargs
├── lambda.py        # Example of map() with a regular function
├── lambda1.py       # Example of map() with string checking
├── lambda2.py       # Examples of filter()
├── lambda3.py       # Examples of lambda with map() and filter()
├── main.py          # Basic PyCharm starter script
├── new.py           # Combined example of *args and **kwargs
├── scope.py         # Example of local and global variable scope
└── test.py          # String length and indexing practice
Requirements
Python 3.x

No external libraries are required.

How to run

Clone the repository:

git clone https://github.com/VictoriaRudakova/DataScience.git
cd DataScience

Run any script with Python:

python args_kwargs.py

or:

python lambda3.py

On some systems, you may need to use:

python3 lambda3.py
Examples
*args and **kwargs

The repository contains examples of functions that accept a variable number of arguments:

def func_with_kwargs(**kwargs):
    print(kwargs)

func_with_kwargs(first=1, second=2, third=3)

And:

def func_with_args(*args):
    print(args)

func_with_args(1, 2, 3)
map()

Example of applying a function to every item in a list:

def sum_of_two_numbers(x):
    return x + x

number_list = [1, 2, 3, 4, 5, 6, 7]

print(list(map(sum_of_two_numbers, number_list)))
filter()

Example of filtering odd numbers:

def is_number_odd(number):
    return number % 2 == 1

number_list = [1, 2, 3, 4, 5, 6, 7]

print(list(filter(is_number_odd, number_list)))
Lambda expression

Example of using lambda with map() and filter():

number_list = [1, 2, 3, 4, 5, 6, 7]

print(list(map(lambda number: number ** 3, number_list)))
print(list(filter(lambda number: number % 2 == 1, number_list)))
Notes

This repository is intended for Python practice and learning.
It is not a production data science project yet, but it can be expanded later with:

NumPy examples
Pandas examples
Matplotlib visualizations
Jupyter notebooks
Data cleaning tasks
Machine learning experiments
Small data analysis projects
Future improvements
Add folders by topic
Rename files to more descriptive names
Add comments explaining each example
Add Jupyter notebooks for data science practice
Add a requirements.txt file when external libraries are used
Add small datasets for practice
Add examples with Pandas, NumPy and visualization libraries

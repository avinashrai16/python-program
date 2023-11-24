# Explain the purpose of the `map()` function in Python
# and provide an example of how it can be used to apply a function to each element of an iterable.

##

# The map() function in Python is a built-in function
# that is used to apply a specified function to all items in an iterable (e.g., a list, tuple, or string)
# and return an iterator that produces the results.

##

# The basic syntax of the map() function is as follows:
# map(function, iterable, ...)
#
# function: The function to apply to each item of the iterable.
# iterable: The iterable whose elements will be processed by the function.
# Here's a simple example to illustrate the usage of map():
# Define a function that converts an integer to its string representation
# def int_to_str(num):
#     return str(num)
#
#
# # Create a list of integers
# integer_list = [10, 20, 30, 40, 50]
#
# # Use map() to apply the int_to_str function to each element of the list
# string_list = map(int_to_str, integer_list)
#
# # Convert the result to a list
# result_list = list(string_list)
#
# # Print the result
# print(result_list)
# In this example, the int_to_str function is applied to each element of the integer_list using map(),
# resulting in a new list (result_list) containing the string representations of the integers.


#  2 Write a Python program that uses the `map()` function to square each element of a list of numbers.
# Define a function that squares a number
# def square(x):
#     return x ** 2
#
#
# # Create a list of numbers
# numbers = [1, 2, 3, 4, 5]
#
# # Use map() to apply the square function to each element of the list
# squared_numbers = map(square, numbers)
#
# # Convert the result to a list (as map returns an iterator)
# result_list = list(squared_numbers)
#
# # Print the result
# print(result_list)


# 3 How does the `map()` function differ from a list comprehension in Python, and when would you choose one over the other?
# Both map() and list comprehensions in Python are used to perform operations on elements of an iterable,
# but they have some differences in terms of syntax and use cases.
#
# map() function:
# Syntax: map(function, iterable, ...)
# Returns: An iterator (in Python 3) that produces the results of applying the specified function to each item in the iterable.
# Use Case: Typically used when you have an existing function that you want to apply to all elements of an iterable.
# Example using map():
#
# python
# Copy code
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(lambda x: x ** 2, numbers)
# result_list = list(squared_numbers)
# print(result_list)
# # Output: [1, 4, 9, 16, 25]
# List comprehension:
# Syntax: [expression for item in iterable if condition] (with an optional if condition)
# Returns: A new list created by evaluating the expression for each item in the iterable.
# Use Case: Useful when you want to create a new list by specifying the transformation to be applied to each element of an iterable.
# It's often more concise than using map().
# Example using list comprehension:
#
# python
# Copy code
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = [x ** 2 for x in numbers]
# print(squared_numbers)
# # Output: [1, 4, 9, 16, 25]
# Choosing between map() and list comprehension:
# Readability: List comprehensions are often more readable and concise, especially for simple operations.
# If the transformation logic is straightforward, a list comprehension may be a more Pythonic choice.
#
# Function Application: If you have an existing function that you want to apply to each element,
# or if the operation is more complex and involves multiple lines of code, map() with a function
# or a lambda function may be more appropriate.
#
# Lazy Evaluation: map() returns an iterator, which means it produces values on demand.
# This can be more memory-efficient if you're working with large datasets. List comprehensions,
# on the other hand, create the entire list in memory.
#
# Conditionals: List comprehensions support conditional statements, making them more flexible in some cases.
# You can include an if statement to filter elements based on a condition.
#
# In summary, choose between map() and list comprehensions based on readability, simplicity, and the specific requirements of your task.
# For simple transformations, list comprehensions are often preferred, while map() may be more suitable for more complex operations
# or when working with large datasets due to its lazy evaluation nature.


# 4. Create a Python program that uses the `map()` function to convert a list of names to uppercase.
input_list = ["name1", "name2", "name3"]
def make_upper(string):
    return string.upper()

upper_case_list = list(map(make_upper, input_list))
print((upper_case_list))
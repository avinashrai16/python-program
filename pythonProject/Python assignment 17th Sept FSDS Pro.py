# 2. Write a Python program to calculate the factorial of a number using recursion.
# def factorial_iterative(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
#
# number = 5
# result_iterative = factorial_iterative(number)
# print(result_iterative)


#  3. Create a recursive Python function to find the nth Fibonacci number.

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# result = fibonacci(10)
# print("The 10th Fibonacci number is:", result)
# print(fibonacci(10))


#  4. Write a recursive Python function to calculate the sum of all elements in a list.
# def list_sum_recursive(lst):
#     # Base case: an empty list has a sum of 0
#     if not lst:
#         return 0
#     else:
#         return lst[0] + list_sum_recursive(lst[1:])
#
# my_list = [1, 2, 3, 4, 5]
# result = list_sum_recursive(my_list)
# print("The sum of elements in the list is:", result)

#  5. How can you prevent a recursive function from running indefinitely, causing a stack overflow error?

# To prevent a recursive function from running indefinitely and causing a stack overflow error, you can take the following measures:
#
# 1. Base Case:
# Ensure that your recursive function has a base case that defines when the recursion should stop.
# The base case represents the simplest scenario where the function does not make a recursive call but returns a known value.
#
# 2. Ensure Progress Toward the Base Case:
# In each recursive call, make sure the input to the function moves closer to the base case.
# If the input remains the same or moves away from the base case, the function might run indefinitely.

# 3. Check Input Validity:
# Before making a recursive call, check that the input is within valid bounds or meets certain criteria.
# If the input is not valid, you might want to return a specific value or handle it in a way that prevents further recursion.

# 6. Create a recursive Python function to find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.
# def gcd_euclidean(a, b):
#     print(a, b)
#     # Base case
#     if b == 0:
#         return a
#     else:
#         # Recursive case
#         return gcd_euclidean(b, a % b)
#
# # Example: Find the GCD of two numbers
# num1 = 18
# num2 = 48
# result = gcd_euclidean(num1, num2)
# print(f"The GCD of {num1} and {num2} is:", result)

# 7. Write a recursive Python function to reverse a string.

# def reverse(str):
#     if len(str) == 1:
#         return str
#     else:
#         return str[-1]+reverse(str[:-1])
#
# str = "Avinash"
# print(reverse(str))


# 8. Create a recursive Python function to calculate the power of a number (x^n).

# def power(num, pow):
#     if pow == 0:
#         return 1
#     else:
#         return num * power(num, pow - 1)
#
# print(power(3, 3))

# 9. Write a recursive Python function to find all permutations of a given string.
# def get_permutations(s):
#     # Base case: if the string has only one character, return it as a single-element list
#     if len(s) == 1:
#         return [s]
#
#     # Recursive case: find permutations for the string excluding each character
#     all_permutations = []
#     for i in range(len(s)):
#         current_char = s[i]
#         remaining_chars = s[:i] + s[i+1:]
#         print(remaining_chars)
#         permutations_of_remaining = get_permutations(remaining_chars)
#
#         # Combine the current character with each permutation of the remaining characters
#         for perm in permutations_of_remaining:
#             all_permutations.append(current_char + perm)
#
#     return all_permutations
#
# # Example: Find all permutations of the string "abc"
# result = get_permutations("abc")
# print("All permutations:", result)


# 10.	Write a recursive Python function to check if a string is a palindrome.

# def reverse(str):
#     if len(str) == 1:
#         return str
#     else:
#         return str[-1]+reverse(str[:-1])
#
# str = "AvA"
# print("String is palindrome" if str == reverse(str) else "String is not palindrome")

# 11.	Create a recursive Python function to generate all possible combinations of a list of elements.
# def generate_combinations(elements, current_combination=None, index=0, result=None):
#     if current_combination is None:
#         current_combination = []
#     if result is None:
#         result = []
#
#     if index == len(elements):
#         result.append(list(current_combination))
#         return
#
#     current_combination.append(elements[index])
#     generate_combinations(elements, current_combination, index + 1, result)
#
#     current_combination.pop()
#     generate_combinations(elements, current_combination, index + 1, result)
#
#     return result
#
# elements = [1, 2, 3]
# combinations = generate_combinations(elements)
# print(combinations)


# Basics of Functions:
#
#
# 1.	What is a function in Python, and why is it used?
# In Python, a function is a reusable block of code that performs a specific task or set of tasks.
# It allows you to organize code into manageable and modular pieces, making it easier to understand, maintain, and reuse.
# Functions in Python follow a specific syntax, typically defined using the def keyword,
# followed by the function name, parameters in parentheses, a colon, and the function body indented below.
#
# Functions are used for several reasons:
#
# Code Reusability:
# Once you define a function, you can use it in different parts of your program without having to rewrite the same code.
#
# Modularity:
# Functions allow you to break down your code into smaller, more manageable pieces.
# Each function can focus on a specific task, making the overall structure of your program more organized.
#
# Readability:
# Functions make your code more readable and understandable by providing a clear structure and separating different parts of the program.
#
# Abstraction:
# Functions allow you to abstract away the implementation details of a specific task.
# When you call a function, you don't need to know how it achieves its goal; you only need to know what it does.
#
# Testing and Debugging:
# Functions make it easier to test and debug your code. You can isolate specific functionality in a function and test it independently.
#
# In summary, functions are a fundamental concept in Python and programming in general, offering a way to structure and organize code for better readability, maintainability, and reusability.


# 2.	How do you define a function in Python? Provide an example.
#  Here's a simple example of a Python function:
# def greet(name):
#     """This function greets the person passed in as a parameter."""
#     print("Hello, " + name + "!")
#
#
# # Calling the function
# greet("Avinash")


# def is the keyword used to define a function.
# greet is the name of the function.
# (name) is the parameter the function takes. In this case, the function expects one argument, which is a person's name.
# The indented block under the def statement is the function body. It contains the code that the function executes when called.
# The """docstring""" is a documentation string that provides information about the function.
# It is optional but is good practice to include to document the purpose of the function.


# 3.	Explain the difference between a function definition and a function call.
# In Python, a function definition and a function call serve distinct purposes in the life cycle of a function.
#
# Function Definition:
# # A function definition is the process of creating a function.
# It involves specifying the details of what the function does, what parameters it takes, and what it returns.
# # It starts with the def keyword, followed by the function name, a pair of parentheses containing parameters (if any),
# a colon, and a block of code that makes up the function body.
#
# Here's an example of a function definition:
# # def add_numbers(a, b):
#     """This function adds two numbers."""
#     result = a + b
#     return result
# In this example, add_numbers is the function name, (a, b) are the parameters,
# and the indented block below contains the code to add the two numbers.
#
# Function Call:
# # A function call is the process of using a function after it has been defined.
# It involves invoking the function to execute the code within its body.
#
# It is done by using the function name followed by parentheses containing the arguments (if any) required by the function.
# The arguments are the actual values or variables that the function will use when it runs.
#
# Here's an example of a function call using the previously defined add_numbers function:
#
# result = add_numbers(5, 7)
# In this example, add_numbers(5, 7) is the function call.
# It passes the values 5 and 7 as arguments to the function, and the result of the function (the sum of the two numbers) is stored in the variable result.
#
# In summary, the function definition is where you specify what a function does and how it does it,
# while the function call is where you actually use the function, providing specific values or variables for it to work with.
# The definition is a one-time setup that outlines the structure and behavior of the function, while the call is the actual execution of that function with specific inputs.


# 4.	Write a Python program that defines a function to calculate the sum of two numbers and then calls the function.
# function definition:
# def add_numbers(a, b):
#     """This function adds two numbers."""
#     result = a + b
#     return result
#
#
# # function call:
# result = add_numbers(5, 7)
# print(result)


# 5.	What is a function signature, and what information does it typically include?
#
# A function signature refers to the declaration of a function
# and provides information about its name, parameters, return type (if any), and sometimes other details.
# It's a way to convey the essential information about a function without including the entire function body.
# The function signature is often seen in documentation, source code comments, or when discussing a function's interface.
#
# A typical function signature includes the following components:
#
# Function Name:
# The name of the function, which is used to identify and call the function.
#
# Parameters:
# The parameters or arguments that the function accepts.
# These are the values or variables that the function receives when it is called.
# Parameters are enclosed in parentheses and separated by commas.
#
# Return Type:
# The data type of the value that the function returns.
# If a function doesn't return any value, the return type is often specified as None in Python.

# Exceptions (Optional):
#  In some cases, the function signature may include information about the exceptions or errors that the function might raise.
#  This is more common in languages that support explicit exception handling.

# 6. Create a Python function that takes two arguments and returns their product
# function definition:
# def multiply_numbers(a, b):
#     """This function adds two numbers."""
#     result = a * b
#     return result
#
#
# # function call:
# result = multiply_numbers(5, 7)
# print(result)


# Function Parameters and Arguments:
# 1.	Explain the concepts of formal parameters and actual arguments in Python functions.
#
# In Python, formal parameters and actual arguments are terms related to function definitions and function calls, respectively.
#
# Formal Parameters:
# Formal parameters are the placeholders or variables listed in the parentheses of a function definition.
# They represent the input values that a function expects to receive when it is called.
# These parameters act as variables within the function, and their values are supplied by the caller when the function is invoked.
# Formal parameters are defined in the function header and serve as a way for the function to receive input data.
#
# Actual Arguments:
# Actual arguments, also known as arguments or parameters, are the values that are passed to a function when it is called.
# These values are assigned to the corresponding formal parameters inside the function.
# Actual arguments can take different forms, such as positional arguments, keyword arguments, default arguments, and variable-length arguments.
# The number and type of actual arguments must match the number and order of formal parameters declared in the function.

# 2.	Write a Python program that defines a function with default argument values.
# function definition with default argument values :
# def add_num(a=10, b=10):
#     return a+b
#
# # function call , not passing any values as the default values has been defined in the function:
# print(add_num())


# 3.	How do you use keyword arguments in Python function calls? Provide an example.
# In Python, keyword arguments allow you to pass values to function parameters
# by explicitly specifying the parameter names in the function call.
# This provides more clarity and flexibility, especially when dealing with functions that have a large number of parameters
# or when you want to pass values out of order.
#
# Here's an example:
#
# def display_info(name, age, city):
#     print(f"Name: {name}, Age: {age}, City: {city}")
#
# # Using keyword arguments to pass values
# display_info(name="John", age=25, city="New York")
# In this example, the display_info function takes three parameters: name, age, and city.
# When calling the function, keyword arguments are used to specify which value corresponds to which parameter.
# This makes the code more readable and helps avoid mistakes, especially when dealing with functions that have a similar parameter list.


# 4.	Create a Python function that accepts a variable number of arguments and calculates their sum.
# def calculate_sum(*args):
#     total = sum(args)
#     return total
#
# # Example usage
# result = calculate_sum(1, 2, 3, 4, 5)
# result1 = calculate_sum(1, 2, 3)
# result2 = calculate_sum(4, 5, 6, 7)
# result3 = calculate_sum(8, 9)
#
# print(result)
# print(result1)
# print(result2)
# print(result3)

# 5. What is the purpose of the `*args` and `**kwargs` syntax in function parameter lists?
# The *args and **kwargs syntax in function parameter lists are used to handle a variable number of arguments in a more flexible way.
#
# *args (Arbitrary Positional Arguments):
# The *args syntax allows a function to accept a variable number of positional arguments.
# It collects these arguments into a tuple, which can then be processed within the function.
# This is useful when you want to create functions that can take an arbitrary number of
# input values without explicitly specifying the number of parameters.

# **kwargs (Arbitrary Keyword Arguments):
# The **kwargs syntax allows a function to accept a variable number of keyword arguments.
# It collects these arguments into a dictionary, where the keys are the parameter names and the values are the corresponding argument values.
# This is useful when you want to create functions
# that can accept additional named parameters without explicitly defining them in the function signature.
# Example :
# def example_function(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# example_function(name="John", age=25, city="New York")

# Return Values and Scoping:

# 1.	Describe the role of the `return` statement in Python functions and provide examples.
# In Python, the return statement is used to exit a function and return a value to the caller.
# It plays a crucial role in functions as it allows them to compute a result and provide that result to the part of the program that called the function. The return statement can also be used without a value to indicate that a function has finished its execution.
#
# Here are the key aspects of the return statement:
# # Returning a Value:
# A function can use return to send a specific value back to the caller.
# This value can be of any data type, including integers, floats, strings, lists, tuples, dictionaries, or even custom objects.
# Example :
# def add_numbers(x, y):
#     result = x + y
#     return result
#
# sum_result = add_numbers(3, 5)
# print(sum_result)  # Output: 8


# Returning Multiple Values:
# You can use return to return multiple values as a tuple. This is often used to return multiple pieces of data from a function.
# Example:
# def calculate_statistics(numbers):
#     mean = sum(numbers) / len(numbers)
#     variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
#     return mean, variance
#
# data = [1, 2, 3, 4, 5]
# mean_result, variance_result = calculate_statistics(data)
# print(f"Mean: {mean_result}, Variance: {variance_result}")


# Returning None:
# If a function does not have a return statement or has a return statement without a value, it implicitly returns None.
# None is a special object in Python representing the absence of a value.
# Example :
# def simple_function():
#     print("This function does not return anything.")
#
# result = simple_function()
# print(result)  # Output: None


# Exiting a Function Early:
# The return statement can be used to exit a function prematurely.
# This can be useful in situations where further execution of the function is unnecessary.
# It's important to note that a function can have multiple return statements,
# but once the first return statement is encountered, the function exits, and the subsequent code in the function is not executed.
# The return statement is crucial for functions to produce results that can be used elsewhere in a program.)
# def is_positive(number):
#     if number > 0:
#         return True
#     else:
#         return False
#
# result = is_positive(5)
# print(result)  # Output: True


# 2.	Explain the concept of variable scope in Python, including local and global variables.
# In Python, variable scope refers to the region of the code where a particular variable can be accessed or modified.
# The scope of a variable is determined by where it is declared, and it can be classified into two main types: local scope and global scope.

# Local Scope:
# A local variable is declared inside a function or a block of code and is only accessible within that specific function or block.
# The local scope is created when a function is called and is destroyed when the function completes execution.
# Local variables are independent of each other, even if they have the same name in different functions.
# Example:
# def my_function():
#     x = 10  # 'x' is a local variable
#     print(x)
#
#
# my_function()

# Trying to access 'x' outside the function will result in an error
# print(x)  # This will raise a NameError
# Global Scope:
#
# A global variable is declared outside any function or block of code and is accessible throughout the entire program.
# Global variables retain their values across different function calls and are generally used for data that needs to be shared across various parts of the program.
# Modifying the value of a global variable inside a function requires the use of the global keyword.
# Example:

# y = 20  # 'y' is a global variable
#
#
# def another_function():
#     global y
#     y += 5  # Modifying the global variable 'y'
#     print(y)
#
#
# another_function()
# # Output: 25
#
# print(y)
# The value of 'y' is now 25
# Scope Hierarchy:
# Python follows a hierarchy of scopes, known as the LEGB (Local, Enclosing, Global, and Built-in) rule:
# Local (L): Inside the function.
# Enclosing (E): Any enclosing functions, if applicable (for example, if a function is nested inside another function).
# Global (G): At the top level of the module or script.
# Built-in (B): Python's built-in names (e.g., print, len).
# Example:

# z = 30  # 'z' is a global variable
#
#
# def outer_function():
#     z = 40  # 'z' is a local variable inside outer_function
#
#     def inner_function():
#         nonlocal z  # Refers to the 'z' in the enclosing scope (outer_function)
#         z += 5
#         print(z)
#
#     inner_function()
#
#
# outer_function()
# # Output: 45
#
# print(z)
# The value of the global 'z' remains unaffected
# Understanding variable scope is crucial for writing maintainable and bug-free code.
# It helps prevent unintended variable modifications
# and allows for the proper organization of code by limiting the accessibility of variables to the parts of the program where they are needed.

# 3.	Write a Python program that demonstrates the use of global variables within functions.
# Global variable
# global_variable = 10


# def increment_global():
#     # Accessing the global variable
#     global global_variable
#     global_variable += 5
#     print("Inside increment_global function:", global_variable)


# def multiply_global(value):
#     # Accessing the global variable
#     global global_variable
#     result = global_variable * value
#     print("Inside multiply_global function:", result)
#
#
# # Display the initial value of the global variable
# print("Initial global_variable value:", global_variable)
#
# # Call the functions
# increment_global()
# multiply_global(3)
#
# # Display the updated value of the global variable
# print("Final global_variable value:", global_variable)

# 4.Create a Python function that calculates the factorial of a number and returns it.

# def factorial(n):
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result
#
#
# # Example usage:
# number = 5
# result = factorial(number)
# print(f"The factorial of {number} is: {result}")

# 5.	How can you access variables defined outside a function from within the function?
# In Python, you can access variables defined outside a function from within the function by using the global keyword or by directly referencing the variables. The method you choose depends on whether you want to modify the global variable within the function.
#
# Here are two ways to access variables defined outside a function:
# Using the global Keyword:
#
# If you want to modify the value of a global variable within a function, you need to use the global keyword.
# Example:

# global_variable = 10
#
#
# def access_global_variable():
#     global global_variable
#     print("Inside the function:", global_variable)
#
#
# access_global_variable()
# print("Outside the function:", global_variable)

# In this example, the global_variable is accessed both inside and outside the function.
#
# Directly Referencing the Variable:
#
# If you only want to read the value of a global variable within a function (without modifying it),
# you can directly reference the variable without using the global keyword.
# Example:

# global_variable = 10
#
#
# def access_global_variable():
#     print("Inside the function:", global_variable)
#
#
# access_global_variable()
# print("Outside the function:", global_variable)
# In this example, the function access_global_variable prints the value of global_variable without using the global keyword.

# It's important to note that if you want to modify a global variable within a function,
# you must use the global keyword; otherwise, Python will create a new local variable with the same name inside the function.
# Reading the value of a global variable can be done directly without using global.


# Built-in Functions::
# 1.Describe the role of built-in functions like `len()`, `max()`, and `min()` in Python.
# Built-in functions in Python, such as len(), max(), and min(), provide convenient and efficient ways to perform common operations on data structures and values. Here's a brief overview of each:
#
# len() Function:
#
# The len() function is used to determine the length or the number of elements in an object.
# It can be applied to various data types, including strings, lists, tuples, and dictionaries.
# For strings, len() returns the number of characters. For lists, tuples, and other iterable objects, it returns the number of elements.
# Example:
#
# string_length = len("Hello, World!")
# print("String length:", string_length)
#
# list_length = len([1, 2, 3, 4, 5])
# print("List length:", list_length)
# max() and min() Functions:
#
# The max() function returns the largest item in an iterable or the largest of two or more arguments.
# The min() function, on the other hand, returns the smallest item in an iterable or the smallest of two or more arguments.
# Example:
#
# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
#
# max_value = max(numbers)
# min_value = min(numbers)
#
# print("Maximum value:", max_value)
# print("Minimum value:", min_value)
# Both max() and min() can be used with various data types, including numbers, strings, and other comparable objects.
# They are often used in scenarios where you need to find the maximum or minimum value within a collection.
#
# These built-in functions are part of the Python standard library and contribute to the language's expressiveness and ease of use.
# They are efficient and widely used for common tasks, making Python code more concise and readable.


# 2.	Write a Python program that uses the `map()` function to apply a function to each element of a list.

# def square(x):
#     return x ** 2
#
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(square, numbers)
# result_list = list(squared_numbers)
# print("Original Numbers:", numbers)
# print("Squared Numbers:", result_list)

# 3. How does the `filter()` function work in Python, and when would you use it?
# The filter() function in Python is used to construct an iterator from elements of an iterable for which a function returns true.
# It is a powerful built-in function that provides a concise way to filter elements based on a specified condition.
# The syntax of the filter() function is as follows:
# filter(function, iterable)

# you would use the filter() function when you need to extract elements from an iterable based on a specific condition.
# It provides a more concise and readable alternative to using a loop and an if statement to perform the same filtering operation.
# The function passed to filter() defines the condition for inclusion in the result.

# 4.	Create a Python program that uses the `reduce()` function to find the product of all elements in a list.

# from functools import reduce
#
# def multiply(num1, num2):
#     return num1 * num2
#
# list1 = [1, 2, 3, 4, 5]
#
# result = reduce(multiply, list1)
# print(result)


# Function Documentation and Best Practices:
# 1. Explain the purpose of docstrings in Python functions and how to write them.
# In Python, a docstring is a string literal that occurs as the first statement in a module, function, class, or method definition.
# The primary purpose of docstrings is to provide documentation and help for the code.
# They serve as a way to document the purpose, usage, and behavior of functions, classes, and modules, making it easier for developers to understand and use the code.

# A docstring can be a single-line or multi-line string and is typically enclosed in triple double quotes (""").
# It is placed immediately after the function, class, or module definition.
# Here's a simple example of a function with a docstring:

# def add_numbers(x, y):
# """
# Adds two numbers and returns the result.
#
# Parameters:
# - x (int): The first number.
# - y (int): The second number.
#
# Returns:
# - int: The sum of x and y.
# """
# result = x + y
# return result

# In this example:
#
# The docstring is enclosed in triple double quotes.
# It provides a brief description of the function's purpose.
# It documents the parameters (x and y), their types, and any other relevant information.
# It specifies the return type and describes what the function returns.
# Here are some key points about writing docstrings:
#
# Use Triple Quotes:
#
# Always enclose docstrings in triple double quotes (""") for both single-line and multi-line docstrings.
# Be Concise and Clear:
#
# Keep the docstring concise but provide enough information for someone to understand how to use the function or class.
# Include Parameters and Return Values:
#
# Document the parameters, their types, and any other relevant information. Specify the expected return type and describe what the function or method returns.
# Use ReStructuredText Format (Optional):
#


# 2. Describe some best practices for naming functions and variables in Python, including naming conventions and guidelines.

# Naming functions and variables in a clear and consistent manner is crucial for writing readable and maintainable Python code.
# Adhering to naming conventions and following best practices helps improve code clarity
# and makes it easier for others (or your future self) to understand and work with your code.
# Here are some best practices for naming functions and variables in Python:
#
# 1. Use Descriptive Names:
# Choose names that clearly convey the purpose or intent of the function or variable. Avoid overly short or cryptic names.
#
# # Good
# def calculate_total_price(product_price, quantity):
# # Bad
# def calc_tot_prc(p, q):
#
# Follow PEP 8:
# PEP 8 is the official Python style guide, and it provides recommendations for naming conventions. Some key points include:
#
# Use lowercase with underscores for function and variable names (snake_case).
# Use uppercase for constants (ALL_CAPS_WITH_UNDERSCORES).
# Use descriptive and meaningful names.
# Good
# total_price = calculate_total_price(product_price, quantity)
# MAX_RETRIES = 3
# # Bad
# TotalPrice = calc_tot_price(prod_price, qty)

# Be Consistent:
# Maintain consistency in naming across your codebase. If you use a specific naming style, stick to it throughout your project.
#
# Example:
# Consistent naming style
# def process_data(data):
# def analyze_results(results):


# Avoid Single-Letter Variable Names (Unless Appropriate):
# In general, avoid using single-letter variable names unless they represent iterators in short loops.
# Single-letter names are often not descriptive.
# Good (in a short loop)
# for item in items:
# # Bad
# i = 0
# for j in range(len(data)):
#
#
# Use Verb-Noun Naming for Functions:
# For functions, it's often helpful to use a verb-noun naming convention to convey that the function performs an action.
#
# Example:
#  Good
# def calculate_total_price(product_price, quantity):
# # Bad
# def product_quantity_total_price(price, qty):

# Avoid Shadowing Built-in Names:
# Avoid using names that shadow built-in functions or constants, as this can lead to confusion and unexpected behavior.
# Good
# def calculate_sum(numbers):
#     total = sum(numbers)
#     return total
# # Bad (avoid shadowing sum)
# def sum(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total

# Use Plural for Collections:
# When naming variables that represent collections (lists, dictionaries, etc.), use a plural form.
# Example:
# # Good
# students = ["Alice", "Bob", "Charlie"]
# # Bad
# student_list = ["Alice", "Bob", "Charlie"]

# Provide Context:
# Include enough context in your names to make their purpose clear. Avoid generic names that could be ambiguous
# Good
# def calculate_area_of_circle(radius):
# # Bad
# def calculate_area(radius):
# By following these best practices, you contribute to writing clean, understandable, and maintainable Python code.
# Consistency and clarity in naming conventions are essential for effective communication within a development team
# and for the long-term sustainability of a codebase.

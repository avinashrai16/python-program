# For Loop :-
# 1.	Write a Python program to print numbers from 1 to 10 using a for loop.
# for i in range(1, 11):
#     print(i, end=" ")

# 2.	Explain the difference between a for loop and a while loop in Python.
# Key Differences:
# Structure:
# The for loop iterates over a sequence or iterable, and it has a fixed structure for the iteration.
# The while loop iterates as long as a specified condition is true. It has a more flexible structure that depends on the condition.
#
# Initialization and Update:
# In a for loop, the iteration variable is automatically updated for each iteration based on the elements of the iterable.
# In a while loop, you need to initialize the loop variable before the loop and update it within the loop to control the iteration.
#
# Use Cases:
# Use a for loop when you know the number of iterations or when iterating over a sequence or iterable.
# Use a while loop when you want to repeat a block of code until a certain condition is met, and the number of iterations is not known in advance.
#
# Risk of Infinite Loop:
# A poorly constructed while loop may result in an infinite loop if the condition is never met. Care must be taken to ensure that the condition becomes false at some point.
# for loops are less prone to infinite loops because they are based on a fixed sequence, and the loop variable is automatically updated.

# 3. Write a Python program to calculate the sum of all numbers from 1 to 100 using a for loop.

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# 4. How do you iterate through a list using a for loop in Python?
# you can iterate through a list using a for loop.
# The for loop iterates over each element in the list, and you can perform actions on each element during each iteration.
# Here's the basic syntax for a for loop:
# for element in my_list:
# code to be executed for each iteration using 'element'


# Example :
# fruits = ["apple", "banana", "orange"]
#
# for fruit in fruits:
#     print(fruit)

# 5. Write a Python program to find the product of all elements in a list using a for loop.
# product = 1
# for number in range(1, 6):
#     product *= number
# print(product)

# 6. Create a Python program that prints all even numbers from 1 to 20 using a for loop.
# for number in range(1, 21):
#     if number % 2 == 0:
#         print(number, end=" ")

# 7. Write a Python program that calculates the factorial of a number using a for loop.
# num = 5
# factorial = 1
# for i in range(1, num+1):
#     factorial *= i
# print(f"factorial of {num} is {factorial}")

# 8 How can you iterate through the characters of a string using a for loop in Python?
# str = "avinash"
# for char in str:
#     print(char, end=":")

# 9 Write a Python program to find the largest number in a list using a for loop.
# list1 = list(range(1, 11))
# largest_num = 0
# for item in list1:
#     if item > largest_num:
#         largest_num = item
# print(f"{largest_num} is the largest number in {list1}  ")


# 10.	Create a Python program that prints the Fibonacci sequence up to a specified limit using a for loop.
# def fibonacci(limit):
#     fib_sequence = [0, 1]
#
#     for _ in range(2, limit):
#         next_fibonacci = fib_sequence[-1] + fib_sequence[-2]
#
#         if next_fibonacci > limit:
#             break
#
#         fib_sequence.append(next_fibonacci)
#
#     return fib_sequence
#
# limit_level = 6
# print (fibonacci(limit_level))

# 11.	Write a Python program to count the number of vowels in a given string using a for loop.
# vowels = list("AEIOUaeiou")
# str1 = "Write a Python program to count the number of vowels in a given string using a for loop"
# vowel_char_counter = 0
# vowel_char_dec = {}
# for char in str1:
#     if char in vowels:
#         if vowel_char_dec.get(char):
#             temp = {char: vowel_char_dec.get(char)+1}
#             vowel_char_dec.update(temp)
#         else:
#             temp = {char: 1}
#             vowel_char_dec.update(temp)
# print(str1)
# print(f"above string contains vowels {vowel_char_dec}")

# 12.	Create a Python program that generates a multiplication table for a given number using a for loop.
# num = 4
# def table(number):
#     for i in range(1, 11):
#         yield number*i
#
# print(f"below is the table for {num}")
# print(list(table(num)))


# 13.	Write a Python program to reverse a list using a for loop.
# list1 = [1, 2, 3, 4, 5]
# reversed_list1 = []
# for i in range(-1, -(len(list1)+1), -1):
#     reversed_list1.append(list1[i])
#
# print(f"original list:{list1}")
# print(f"reversed list:{reversed_list1}")

# 14. Write a Python program to find the common elements between two lists using a for loop.
# list1 = list(range(1, 11))
# list2 = list(range(1, 6))
# common_element_list = []
# for element in list1:
#     if element in list2:
#         common_element_list.append(element)
#
# print(f"first list:{list1}")
# print(f"second list:{list2}")
# print(f"common elements {common_element_list}")

# 15. Explain how to use a for loop to iterate through the keys and values of a dictionary in Python.
# dic1 = {"firstName": "Avinash", "lastName": "Rai", "DOB": "xx-xx-xxxx"}
# for key, value in dic1.items():
#     print(key, ":", value)


# 16. Write a Python program to find the GCD(Greatest Common Divisor) of two numbers using a for loop.

# def number_divisor(num1, num2):
#     num1_divisor = 1
#     for i in range(1, num1 + 1):
#         if num1 % i == 0:
#             if num2 % i == 0:
#                 if num1_divisor < i:
#                     num1_divisor = i
#     return num1_divisor
#
# print(number_divisor(32, 48))

# 17. Create a Python program that checks if a string is a palindrome using a for loop.
# str1 = "AvA"
# reverse_str1 = ""
# for i in range(-1, -(len(str1)+1), -1):
#     reverse_str1 += str1[i]
#
# print("string is palindrome" if str1 == reverse_str1 else "string is not palindrome")


# 18. Write a Python program to remove duplicates from a list using a for loop.
# list1 = [1, 2, 3, 4, 5, 6, 1, 2, 3]
# unique_list = []
# for i in list1:
#     if i not in unique_list:
#         unique_list.append(i)
#
# print(f"original list {list1}")
# print(f"unique item list {unique_list}")


# 19.	Create a Python program that counts the number of words in a sentence using a for loop.
# sentence = "Create a Python program that counts the number of words in a sentence using a for loop"
# word_counter = 0
# for i in sentence.split():
#     word_counter += 1
#
# print(sentence)
# print(f"has {word_counter} words")


# 20.	Write a Python program to find the sum of all odd numbers from 1 to 50 using a for loop.
# sum_of_odd = 0
# list_of_numbers = list(range(1, 51))
# for number in list_of_numbers:
#     if number % 2 != 0:
#         sum_of_odd += number
#
# print(f"sum of off numbers from 1 to 50 is {sum_of_odd}")

# 21. Write a Python program that checks if a given year is a leap year using a for loop.
# import calendar
# def get_february_calendar(year):
#     february_calendar = calendar.monthcalendar(year, 2)
#     for week in february_calendar:
#         for day in week:
#             if day == 29:
#                 return True
#     return False
#
# year = 2044
#
# if get_february_calendar(year):
#     print(f"given year i.e. {year} is a leap year")
# else:
#     print(f"given year i.e. {year} is not a leap year")


# 22. Create a Python program that calculates the square root of a number using a for loop.
# def square_root_estimate(number, iterations=100):
#     guess = number / 2  # Initial guess, can be improved for better accuracy
#     for _ in range(iterations):
#         guess = 0.5 * (guess + number / guess)
#     return guess
#
# number_to_sqrt = float(input("Enter a number: "))
#
# result = square_root_estimate(number_to_sqrt)
# print(f"The estimated square root of {number_to_sqrt} is approximately {result:.6f}")

# 23.	Write a Python program to find the LCM (Least Common Multiple) of two numbers using a for loop.
# def greatest_number_divisor(num1, num2):
#     num1_divisor = 1
#     for i in range(1, num1 + 1):
#         if num1 % i == 0:
#             if num2 % i == 0:
#                 if num1_divisor < i:
#                     num1_divisor = i
#     return num1_divisor
#
# def lcm(num1, num2):
#     return abs(num1 * num2) // greatest_number_divisor(num1, num2)
#
# number1 = 5
# number2 = 4
# result = lcm(number1, number2)
# print(f"The LCM of {number1} and {number2} is {result}.")


# If else :

# 1.Write a Python program to check if a number is positive, negative, or zero using an if-else statement.
# given_num = 90
# if given_num > 0:
#     print(f" number {given_num} is a positive number")
# elif given_num == 0:
#     print(f" number {given_num} is a zero")
# else:
#     print(f" number {given_num} is a negative number")

# 2. Create a Python program that checks if a given number is even or odd using an if-else statement.
# given_num = 95
# if given_num % 2 == 0:
#     print(f" number {given_num} is a even number")
# else:
#     print(f" number {given_num} is a odd number")

# 3.	How can you use nested if-else statements in Python, and provide an example?
# given_num = 0
# if given_num >= 0:
#     # nested if else
#     if given_num == 0:
#         print(f" number {given_num} is a zero")
#     else:
#         print(f" number {given_num} is a positive number")
# else:
#     print(f" number {given_num} is a negative number")

# 4.	Write a Python program to determine the largest of three numbers using if-else.
# num1, num2, num3 = 4, 5, 4
# largest_num = 0
# if num1 > num2 and num1 > num3:
#     largest_num = num1
# elif num2 > num1 and num2 > num3:
#     largest_num = num2
# elif num3 > num1 and num3 > num2:
#     largest_num = num3
#
# print(f"largest number in {num1, num2, num3} is {largest_num}")


# 5. Write a Python program that calculates the absolute value of a number using if-else.
# num = -23
# if num < 0:
#     absolute_value = -num
# else:
#     absolute_value = num
# print(f"The absolute value of {num} is {absolute_value}.")

# 6.	Create a Python program that checks if a given character is a vowel or consonant using if-else.
# given_char = "z"
# vowel_list = list("aeiou")
# if given_char.lower() in vowel_list:
#     print(f"given char {given_char} is a vowel")
# else:
#     print(f"given char {given_char} is a consonant")


# 7.	Write a Python program to determine if a user is eligible to vote based on their age using if-else.

# def check_age(age):
#     if age >= 18:
#         return True
#     else:
#         return False
# try:
#     input_age = int(input("tell me your age"))
#     if input_age < 0:
#         raise ValueError("negative numbers are not allowed")
#     if check_age(input_age):
#         print(" You are eligible to vote")
#     else:
#         print(" You are not eligible to vote")
#
# except ValueError as ValException:
#     print("only +ve number is a valid input, kindly provide the same")

# 8.	Create a Python program that calculates the discount amount based on the purchase amount using if-else.
# def calculate_discounted_price(purchase_amount):
#     # Define discount rates based on purchase amount
#     if purchase_amount < 50:
#         discount_rate = 0
#     elif purchase_amount < 100:
#         discount_rate = 0.05  # 5% discount for purchases between 50 and 99
#     elif purchase_amount < 200:
#         discount_rate = 0.1   # 10% discount for purchases between 100 and 199
#     else:
#         discount_rate = 0.15  # 15% discount for purchases of 200 or more
#
#     # Calculate the discounted price
#     discounted_price = purchase_amount - (purchase_amount * discount_rate)
#     return discounted_price
#
# # Get user input for the purchase amount
# try:
#     amount = float(input("Enter the purchase amount: ₹"))
#     if amount < 0:
#         print("Invalid input. Please enter a non-negative number.")
#     else:
#         discounted_price = calculate_discounted_price(amount)
#         print(f"The discounted price is: ₹{discounted_price:.2f}")
# except ValueError:
#     print("Invalid input. Please enter a valid numerical value.")


# 9.	Write a Python program to check if a number is within a specified range using if-else.
# number = 81
# specified_range = range(1, 31)
# if number in list(specified_range):
#     print(f" number {number} is part of {list(specified_range)}")
# else:
#     print(f" number {number} is not a part of {list(specified_range)}")

# 10.	Create a Python program that determines the grade of a student based on their score using if-else.
# grading rule
# 1. >75 First division with distinction
# 2. >60 First division <75
# 3. >50 Second division <60
# 4. >35 Third division <50

# student_score_percentage = 70
# if student_score_percentage > 75:
#     print("First division with distinction")
# elif 60 < student_score_percentage < 75 :
#     print("First division")
# elif 50 < student_score_percentage < 60 :
#     print("Third division")


# 11. Write a Python program to check if a string is empty or not using if-else.
# user_input = "Write a Python program to check if a string is empty or not using if-else"
# if len(user_input) == 0:
#     print("The string is empty.")
# else:
#     print("The string is not empty.")

# 12. Create a Python program that identifies the type of a triangle (e.g., equilateral, isosceles, or scalene)
# based on input values using if-else
# x = input("give value of side 1")
# y = input("give value of side 2")
# z = input("give value of side 3")
# print(
#     "Equilateral Triangle" if x == y == z else "Isosceles Triangle" if x == y or y == z or z == x else "Scalene Triangle")

# 13. Write a Python program to determine the day of the week based on a user-provided number using if-else.
# week_dic = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
#
# try:
#     week_day_input = int(input("Enter number of the day, for which you need to know the name : "))
#     if week_day_input > 7 or week_day_input <= 0:
#         raise ValueError("invalid input")
#     else:
#         print(f"name of the day is {week_dic.get(week_day_input)}, for day number {week_day_input} ")
# except ValueError as ValErr:
#     print("Invalid input. Please enter valid week day number between 1 to 7 .")

# 14.Create a Python program that checks if a given year is a leap year using both if-else and a function.
# year_input = 2000
# def year_chk(year):
#     result = ""
#     if year % 4 == 0 and year % 400 == 0:
#         result = 'Year is a Leap Year.'
#     else:
#         result = 'Year is not a Leap Year.'
#
#     return result
#
# print(year_chk(year_input))

# 15. How do you use the "assert" statement in Python to add debugging checks within if-else blocks?

# the assert statement is used for debugging purposes to check whether a given condition is True.
# If the condition is False, an AssertionError exception is raised, providing a convenient way to add debugging checks within if-else blocks.
#
# Here's an example demonstrating the use of assert within an if-else block:
# def divide(a, b):
#     assert b != 0, "Cannot divide by zero"  # Debugging check with assert
#     return a / b
#
# # Example usage
# numerator = float(input("Enter the numerator: "))
# denominator = float(input("Enter the denominator: "))
#
# if denominator != -1:
#     result = divide(numerator, denominator)
#     print(f"The result of {numerator} / {denominator} is {result}")
# else:
#     print("Cannot perform division. Denominator is zero.")


# 16.Create a Python program that determines the eligibility of a person for a senior citizen discount based on age using if-else.
# Input age
# try:
#     age = int(input("Enter your age: "))
#
#     if age >= 60:
#         print("Congratulations! You are eligible for a senior citizen discount.")
#     else:
#         print("Sorry, you are not eligible for a senior citizen discount.")
# except ValueError:
#     print("given input of age is not valid please provide a valid age")


# 17 Write a Python program to categorize a given character as uppercase, lowercase, or neither using if-else.
# input_char = '#'
# if input_char.islower():
#     print("lowercase")
# elif input_char != input_char.lower():
#     print("uppercase")
# else:
#     print("neither")

# 18 Write a Python program to determine the roots of a quadratic equation using if-else.
# import math
#
# # Input coefficients
# a = 23.45
# b = 34.56
# c = 43.76
#
# # Calculate the discriminant
# discriminant = b**2 - 4 * a * c
#
# # Determine the roots using if-else
# if discriminant > 0:
#     # Two distinct real roots
#     root1 = (-b + math.sqrt(discriminant)) / (2 * a)
#     root2 = (-b - math.sqrt(discriminant)) / (2 * a)
#     print(f"The roots are real and distinct: {root1} and {root2}")
# elif discriminant == 0:
#     # One real root (double root)
#     root = -b / (2 * a)
#     print(f"There is one real and repeated root: {root}")
# else:
#     # Complex roots
#     real_part = -b / (2 * a)
#     imag_part = math.sqrt(abs(discriminant)) / (2 * a)
#     print(f"The roots are complex: {real_part} + {imag_part}i and {real_part} - {imag_part}i")


# 19. Create a Python program that checks if a given year is a century year or not using if-else.
# Input a year
# year = 2024
# if year % 100 == 0:
#     if year % 400 == 0:
#         print(f"{year} is a century year.")
#     else:
#         print(f"{year} is not a century year.")
# else:
#     print(f"{year} is not a century year.")

# 20. Write a Python program to determine if a given number is a perfect square using if-else.
# number = 16
# if number >= 0:
#     square_root = int(number**0.5)
#     if square_root**2 == number:
#         print(f"{number} is a perfect square.")
#     else:
#         print(f"{number} is not a perfect square.")
# else:
#     print("Please enter a non-negative number.")

# 21. Explain the purpose of the "continue" and "break" statements within if-else loops.
# The continue and break statements are control flow statements in Python that are used within loops (including for and while loops)
# to alter the normal execution flow.

# continue statement:
# The continue statement is used to skip the rest of the code inside a loop for the current iteration and jump to the next iteration.
# It is typically used when you want to skip some part of the loop's code based on a certain condition.

# break statement:
# The break statement is used to exit a loop prematurely, regardless of the loop condition.
# It is often used when a certain condition is met, and there is no need to continue iterating through the rest of the loop.

# In summary:
# continue is used to skip the rest of the loop code for the current iteration and move on to the next iteration.
# break is used to exit the loop prematurely when a certain condition is met, regardless of the loop condition.

# 22. Create a Python program that calculates the BMI (Body Mass Index) of a person based on their weight and height using if-else.
# def calculate_bmi(weight, height):
#     bmi = weight / (height ** 2)
#     # Determine the BMI category
#     if bmi < 18.5:
#         category = "Underweight"
#     elif 18.5 <= bmi < 25:
#         category = "Normal weight"
#     elif 25 <= bmi < 30:
#         category = "Overweight"
#     else:
#         category = "Obese"
#
#     return bmi, category
#
# weight = float(input("Enter your weight in kilograms: "))
# height = float(input("Enter your height in meters: "))
#
# bmi, category = calculate_bmi(weight, height)
#
# print(f"Your BMI is: {bmi:.2f}")
# print(f"You are in the '{category}' category.")


# 23. How can you use the "filter()" function with if-else statements to filter elements from a list?
# numbers = [3, 5]
# def is_even(num):
#     return num % 2 == 0
# print("Original list:", numbers)
# if len(numbers) > 0:
#     filtered_numbers = filter(is_even, numbers)
#     filtered_numbers_list = list(filtered_numbers)
#     if len(filtered_numbers_list) > 0:
#         print("Filtered list (even numbers):", filtered_numbers_list)
#     else:
#         print("Filtered list does not have any even numbers:", filtered_numbers_list)


# 24.	Write a Python program to determine if a given number is prime or not using if-else.
def is_prime(number):
    # Check if the number is less than 2 (prime numbers start from 2)
    if number < 2:
        return False
    # Check if the number is exactly 2 (the only even prime number)
    elif number == 2:
        return True
    # Check if the number is divisible by any integer from 2 to the square root of the number
    else:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

# Get user input for the number
try:
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
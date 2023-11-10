# --- Basic if else --- #

# Q1. if a given number is positive or negative
"""
def check_num(int1):
    if abs(int1) == int1:
        print("positive")
    else:
        print("negative")


try:
    input_num = int(input("give a number"))
    check_num(input_num)
except ValueError as ValException:
    print("only number is valid input, kindly provide the same")
"""

# Q2.Eligible for voting ?

"""
def check_age(age):
    if age >= 18:
        return True
    else:
        return False


try:
    input_age = int(input("tell me your age"))
    if input_age < 0:
        raise ValueError("negative numbers are not allowed")
    if check_age(input_age):
        print(" You are eligible to vote")
    else:
        print(" You are not eligible to vote")

except ValueError as ValException:
    print("only +ve number is a valid input, kindly provide the same")
"""

# Q3.Develop a Program to find the maximum of two numbers using if else statements
"""
def check_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


try:
    input_num1 = int(input("tell me first number"))
    input_num2 = int(input("tell me second number"))

    print(f" the bigger number between {input_num1} and {input_num2} is {check_max(input_num1, input_num2)}")
except ValueError as ValException:
    print("only number is valid input, kindly provide the same")

"""

# Q4. Leap year check
"""
input_year = 2004

print("the given year is a leap year" if input_year % 4 == 0 else "the given year is not a leap year")
"""

# Q5. Char is vowel or not
"""
input_char = "z"
vowel_str = "aeiouAEIOU"
print("the given char is a vowel" if input_char in vowel_str else "the given char is a consonant")
"""

# Q6. Even or odd
""" 
input_num = 53
print("the given number is even" if input_num % 2 == 0 else "the given number is odd")
"""

# Q7. absolute value of a number without using abs ()
"""
def my_abs(num1):
    if num1 > num1 * 2:  # negative number case
        return num1 - (num1 + num1)

    else:  # positive number case
        return num1


input_num1 = -10
print(my_abs(input_num1))
"""

# Q8. largest of 3 given numbers
"""
num1, num2, num3 = 8, 9, 70

if num1 > num2 and num1 > num3:
    print(f"largest number is {num1}")

elif num2 > num1 and num2 > num3:
    print(f"largest number is {num2}")

else:
    print(f"largest number is {num3}")
"""

# Q9. Palindrome check for a string
"""
input_str = "aa"
print("Given string is Palindrome" if input_str == input_str[::-1] else "Given string is not Palindrome")
"""

# Q10. Grade based on student score
# grading rule
# 1. >75 First division with distinction
# 2. >60 First division <75
# 3. >50 Second division <60
# 4. >35 Third division <50
"""
student_score_percentage = 70
print("First division with distinction" if student_score_percentage > 75
      else "First division" if 60 < student_score_percentage < 75
else "Second division" if 50 < student_score_percentage < 60 else "Third division")
"""
# --- Nested if else --- #
# Q11. Largest among 3 numbers
"""
num1, num2, num3 = 800, 80, 8

if num1 > num2:
    if num1 > num3:
        print(f"largest number is {num1}")
    else:
        print(f"largest number is {num3}")
else:
    if num2 > num3:
        print(f"largest number is {num2}")
    else:
        print(f"largest number is {num3}")
"""
# Q12. Program To Check whether a Triangle is Equilateral, Isosceles or Scalene
"""
def check_triangle(x, y, z):
    # _Check for equilateral triangle
    if x == y == z:
        print("Equilateral Triangle")

    # Check for isosceles triangle
    elif x == y or y == z or z == x:
        print("Isosceles Triangle")

    # Otherwise scalene triangle
    else:
        print("Scalene Triangle")

# Driver Code

# Given sides of triangle
x = 8
y = 8
z = 8
print("Equilateral Triangle" if x == y == z else "Isosceles Triangle" if x == y or y == z or z == x else "Scalene Triangle")
"""
# Q13. leap and century year
"""
year_input = 2004

if year_input % 4 == 0 and year_input % 100 != 0:
    print(f"the given year is a leap year belongs to {year_input // 100 + 1} century but it is not a century year.")
elif year_input % 4 != 0 and year_input % 100 == 0:
    print(f"the given year is a century year belongs to {year_input // 100 + 1} century but it is not a leap year.")
elif year_input % 4 == 0 and year_input % 100 == 0:
    print(f"the given year is a century year belongs to {year_input // 100 + 1} century and it is a leap year as well.")
else:
    print(f"the given year neither a century year nor leap year , but it belongs to {year_input // 100 + 1} century.")
"""

# Q14. Check if number is positive, negative or zero
given_num = 0

print("Positive" if given_num > 0 else "Negative" if given_num < 0 else "Zero")

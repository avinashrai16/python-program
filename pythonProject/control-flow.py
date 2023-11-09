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


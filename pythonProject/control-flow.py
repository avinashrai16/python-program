# 1.Write a program to reverse a string.

# input_str = input("give me a string to reverse")
#
# print(f"the given string is {input_str}")
# print(f"the reverse of the string is {input_str[::-1]}")

# 2. Check if a string is a palindrome.
# input_str = input("give me a string to check palindrome")
# print("the given string is palindrome" if input_str == input_str[::-1] else "the given string is not palindrome")


# 3. Convert a string to uppercase.
# input_str = input("give me a string to convert it into uppercase")
# print(f"the given string is {input_str}")
# print(f"the uppercase of the string is {input_str.upper()}")

# 4. Convert a string to lowercase.
# input_str = input("give me a string to convert it into lowercase")
# print(f"the given string is {input_str}")
# print(f"the lowercase of the string is {input_str.lower()}")


# 5. Count the number of vowels in a string.
# input_str = input("give me a string to count the number of vowels")
# vowel_str = "aeiouAEIOU"
# print(f"the given string is {input_str}")
# vowel_count = len([x for x in input_str if x in vowel_str])
# print(f" the given string {input_str} has {vowel_count} vowel")

# 6 . Count the number of consonants in a string.
# input_str = input("give me a string to count the number of vowels")
# vowel_str = "aeiouAEIOU"
# print(f"the given string is {input_str}")
# consonant_count = len([x for x in input_str if x not in vowel_str])
# print(f" the given string {input_str} has {consonant_count} consonant")

# 7 . Remove all whitespaces from a string.
# input_str = input("give me a string with some whitespace")
# print(f"the given string is {input_str}")
# trimmed_str = "".join([x for x in input_str if x != " "])
# print(f"the trimmed string is:{trimmed_str}")

# 8. Find the length of a string without using the `len()` function.
# input_str = input("give me a string for calculating it's length")
# print(f"the given string is {input_str}")
# char_counter = 0
# for char in input_str:
#     char_counter = char_counter+1
# print(f"length of the given string is :{char_counter}")

# 9. Check if a string contains a specific word.
# input_str = "sample string to check for a word"
# input_word = input(f"give me a word from string '{input_str}'")
# print("given matching word :", input_word)
# print("Matching word found" if len([word for word in input_str.split() if input_word == word]) > 0 else "Matching word not found")

# 10 . Replace a word in a string with another word.
# input_str = "sample string to check for a word"
# input_match_word = input(f"give me a word from string '{input_str}' to match ").strip()
# input_replace_word = input(f"give me a word, with which matching word need to be replaced").strip()
# filtered_str = " ".join([word if input_match_word != word else input_replace_word for word in input_str.split()])
# print(filtered_str)

# 11. Count the occurrences of a word in a string.
# input_str = "sample string to check for a word"
# input_match_word = input(f"give me a word from string '{input_str}' to match ").strip()
# print(f"given word '{input_match_word}' is present {len([word for word in input_str.split() if input_match_word == word])} times in '{input_str}'")

# 12. Find the first occurrence of a word in a string.
# input_str = "sample string to check for a word"
# input_match_word = input(f"give me a word from string '{input_str}' to find the first occurrence ").strip()
# print(f"first occurrence of {input_match_word} is at {input_str.find(input_match_word)}")

# 13. Find the last occurrence of a word in a string.
# input_str = "sample string to check for a word.sample string to check for a word"
# input_match_word = input(f"give me a word from string '{input_str}' to find the last occurrence ").strip()
# print(f"last occurrence of {input_match_word} is at {input_str.rfind(input_match_word)}")

# 14. Split a string into a list of words.
# input_str = "sample string to check for a word."
# print(f"words present in the string '{input_str}' are {input_str.split()}")

# 15. Join a list of words into a string.
# list_of_word = ['sample', 'string', 'to', 'check', 'for', 'a', 'word.']
# created_str = " ".join(list_of_word)
# print("list of words ", list_of_word)
# print("created string", created_str)

# 16. Convert a string where words are separated by spaces to one where words are separated by underscores.
# input_str = "sample string to check for a word.sample string to check for a word"
# updated_str = input_str.replace(" ", "#")
# print(updated_str)

# 17. Check if a string starts with a specific word or phrase.
# input_str = "for a word. sample string to check for a word"
# print(input_str.startswith("sample string to check"))

# 18. Check if a string ends with a specific word or phrase.
# input_str = "Test for a word. Sample string to check for a word"
# print(input_str.endswith("for a word"))

# 19. Convert a string to title case (e.g., "hello world" to "Hello World").
# input_str = "hello world"
# print(input_str.title())

# 20. Find the longest word in a string.
# input_str = "Sample string to check for a"
# print(f"longest word is {max(input_str.split(), key=len)}")

# 21. Find the shortest word in a string.
# input_str = "Sample string to check for a"
# print(f"longest word is {min(input_str.split(), key=len)}")

# 22. Reverse the order of words in a string.
# input_str = "Sample string to check for a"
# updated_str = " ".join(input_str.split()[::-1])
# print(updated_str)

# 23 .Check if a string is alphanumeric.
# input_str = "Sample string"
# print(f"is given string is alphanumeric ? {input_str.isalnum()}")

# 24. Extract all digits from a string.
# input_str = "Sample333 string13123"
# digit_list = [digit for digit in input_str if digit.isnumeric()]
# print(f"digit list  in '{input_str}' is {digit_list}")

# 25. Extract all alphabets from a string.
# input_str = "Sample333 string13123"
# alphabets_list = [alphabet for alphabet in input_str if alphabet.isalpha()]
# print(f"digit list  in '{input_str}' is {alphabets_list}")

# 26. Count the number of uppercase letters in a string.
# input_str = "Sample333 string13123"
# uppercase_list = [alphabet for alphabet in input_str if alphabet.isupper()]
# print(f"digit list  in '{input_str}' is {uppercase_list}")

# 27 . Count the number of lowercase letters in a string.
# input_str = "Sample333 string13123"
# lowercase_list = [alphabet for alphabet in input_str if alphabet.islower()]
# print(f"digit list  in '{input_str}' is {lowercase_list}")

# 28 . Swap the case of each character in a string.
# input_str = "Sample333 string13123"
# swap_case_str = "".join([alphabet.upper() if alphabet.islower() else alphabet.lower() for alphabet in input_str])
# print(f"Swap case string for input string '{input_str}' is {swap_case_str}")

# 29. Remove a specific word from a string.
# input_str = "sample string to check for a word."
# word_to_remove = "check"
# updated_str = " ".join([word for word in input_str.split() if word != word_to_remove])
# print(f"updated string is {updated_str}")

# 30. Check if a string is a valid email address.
# input_email_id = "testte@st..com"
# # simple validation if given email has @ .
# email_id_rule1 = "@."
# email_id_rule2 = "."
# print("email id is valid "
#       if len([x for x in input_email_id if x in email_id_rule1]) > 0 + len([x for x in input_email_id if x in email_id_rule2]) > 0
#       else "email not valid")

# 31. Extract the username from an email address string.
# input_email_id = "test@test.com"
# print(f" the user name is '{input_email_id.split('@')[0]}' in the email id '{input_email_id}'")

# 32 .Extract the domain name from an email address string.
# input_email_id = "test@test.com"
# print(f" the domain name is '{input_email_id.split('@')[1]}' in the email id '{input_email_id}'")

# 33. Replace multiple spaces in a string with a single space.
# input_string_with_space = "test  string  with  double   or    triple  or more than    that    spaces as   well    between  words"
# print(f"update string '{' '.join(input_string_with_space.split())}' ")  # join the words with single space between words

#  34. Check if a string is a valid URL.
# from urllib.parse import urlparse
#
#
# def is_valid_url(url):
#     try:
#         result = urlparse(url)
#         # print(result)
#         return all([result.scheme, result.netloc])
#     except ValueError:
#         return False
#
#
# url1 = "https://www.example.com"
# url2 = "not_a_valid_url"
#
# print(is_valid_url(url1))  # Output: True
# print(is_valid_url(url2))  # Output: False

# 35. Extract the protocol (http or https) from a URL string.
# url_string = "https://learn.pwskills.com/"
# print(f" the protocol is '{url_string.split(':')[0]}' as per the given URL'{url_string}'")

# 36. Find the frequency of each character in a string.
# string_input = "Find the frequency of each character in a string"
# char_dic = {}
# for char in string_input.lower():  # making string case-insensitive
#     if char in list(char_dic.keys()):
#         char_dic.update({char: char_dic.get(char) + 1})
#     else:
#         char_dic.update({char: 1})
# print(f"frequency of each character{char_dic}")

# 37. Remove all punctuation from a string.

# import string
#
# def remove_punctuation(input_string):
#     # Create a translation table
#     translator = str.maketrans('', '', string.punctuation)
#     print(translator)
#     # Use the translation table to remove punctuation
#     result_string = input_string.translate(translator)
#
#     return result_string
#
# input_text = "Hello, world! This is an example text with punctuation."
#
# output_text = remove_punctuation(input_text)
# print(output_text)

# 38. Check if a string contains only digits.
# input_text = "hello 31231132412341234"
# str_check = True
# for char in input_text:
#     if not char.isdigit():
#         str_check = False
#         break
#     else:
#         continue
# print("String contains only digits" if str_check else "string contains not only digits but other characters as well")

# 39. Check if a string contains only alphabets.
# input_text = "hello"
# str_check = True
# for char in input_text:
#     if not char.isalpha():
#         str_check = False
#         break
#     else:
#         continue
# print("String contains only alphabets" if str_check else "string contains not only alphabets but other characters as well")

# 40. Convert a string to a list of characters.
# input_text = "hello"
# print(f"list of characters in the string is {[char for char in input_text]}")

# 41. Check if two strings are anagrams.
# str1, str2 = "debit card", "bad credit"
# anagrams_chk = True
# for item in set(str1):
#     if str1.count(item) != str2.count(item):
#         anagrams_chk = False
#         break
# if anagrams_chk:
#     print(f"Strings '{str1}' and '{str2}' are anagrams")
# else:
#     print(f"Strings '{str1}' and '{str2}' are not anagrams")

# 42. Encode a string using a Caesar cipher.
# def caesar_cipher_encrypt(text, shift):
#     result = ""
#     for char in text:
#         if char.isalpha():  # Check if the character is a letter
#             # Determine the case (uppercase or lowercase) of the character
#             if char.isupper():
#                 result += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
#             else:
#                 result += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
#         else:
#             result += char  # Non-alphabetic characters remain unchanged
#
#     return result
#
#
# plaintext = "Hello, World!"
# shift_value = 3
#
# encrypted_text = caesar_cipher_encrypt(plaintext, shift_value)
# print("Original:   ", plaintext)
# print("Encrypted:  ", encrypted_text)

# 43. Decode a Caesar cipher encoded string.
# def caesar_cipher_decrypt(text, shift):
#     result = ""
#
#     for char in text:
#         if char.isalpha():  # Check if the character is a letter
#             # Determine the case (uppercase or lowercase) of the character
#             if char.isupper():
#                 result += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
#             else:
#                 result += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
#         else:
#             result += char  # Non-alphabetic characters remain unchanged
#
#     return result
#
#
# encrypted_text = "Khoor, Zruog!"
# shift_value = 3
# decrypted_text = caesar_cipher_decrypt(encrypted_text, shift_value)
# print("Encrypted:  ", encrypted_text)
# print("Decrypted:  ", decrypted_text)

# 44. Find the most frequent word in a string.
# string_text = "Hello World Hello Everyone"
# counter = 0
# frequent_word = ""
# for word in string_text.split():
#     if string_text.count(word) > counter:
#         counter = string_text.count(word)
#         frequent_word = word
# print(f"frequent word '{frequent_word}' with count {counter}")

# 45. Find all unique words in a string.
# string_text = "Hello World Hello Everyone"
# print(f"unique words '{set(string_text.split())}'")

# 46. Count the number of syllables in a string.
# import syllables
#
#
# def count_syllables(word):
#     return syllables.estimate(word)
#
#
# def count_syllables_in_text(text):
#     words = text.split()
#     total_syllables = sum(count_syllables(word) for word in words)
#     return total_syllables
#
#
# text = "Hello, how are you doing today?"
# syllable_count = count_syllables_in_text(text)
#
# print(f"The number of syllables in the text is: {syllable_count}")

# 47. Check if a string contains any special characters.
# import re
# def contains_special_characters(input_string):
#     # Define a regular expression pattern for special characters
#     pattern = re.compile(r'[^a-zA-Z0-9\s]')
#
#     # Check if the pattern matches any part of the input string
#     return bool(pattern.search(input_string))
#
# test_string1 = "Hello123"
# test_string2 = "Hello@World!"
#
# print(contains_special_characters(test_string1))  # Output: False
# print(contains_special_characters(test_string2))  # Output: True

# 48. Remove the nth word from a string.
# input_text = "Hello how are you doing today?"
# nth_word_position = 3
# try:
#     nth_word = input_text.split()[nth_word_position]
#     print(nth_word)
#     print(input_text.replace(nth_word, ""))
#
# except IndexError:
#     print(IndexError)

# 49. Insert a word at the nth position in a string.
# input_text = "Hello how are  doing today?"
# nth_word_position = 3
# nth_word = "you"
# try:
#     input_text1 = input_text.split()
#     input_text1.insert(nth_word_position, nth_word)
#     print(" ".join(input_text1))
#
# except IndexError:
#     print(IndexError)

# 50. Convert a CSV string to a list of lists.
# csv_string = """Name, Age, City
# John, 25, New York
# Jane, 30, London
# Bob, 22, Paris
# """
# data_list = []
# for line in csv_string.splitlines():
#     line_data_list = [line]
#     data_list.append(line_data_list)
# print(data_list)

#  1. Create a list with integers from 1 to 10.
# int_list = list(range(1, 11))
# print(int_list)

# 2. Find the length of a list without using the `len()` function.
# list1 = [1, 2, 3, 54, 56, 57]
# counter = 0
# for item in list1:
#     counter += 1
# print(f"total length of list is {counter}")

# 3. Append an element to the end of a list.
# list1 = [1, 2, 3, 54, 56, 57]
# list1.append(4)
# print(f"updated list {list1}")

# 4. Insert an element at a specific index in a list.
# list1 = [1, 2, 3, 54, 56, 57]
# print(f"before insert {list1}")
# list1.insert(0, 0)
# print(f"after insert {list1}")

# 5. Remove an element from a list by its value.
# list1 = [1, 2, 3, 54, 56, 57]
# print(f"before removal by value {list1}")
# list1.remove(3)
# print(f"after removal by value {list1}")

# 6. Remove an element from a list by its index.
# list1 = [1, 2, 3, 54, 56, 57]
# print(f"before removal by index {list1}")
# list1.pop(2)
# print(f"after removal by index {list1}")

# 7. Check if an element exists in a list.
# list1 = [1, 2, 3, 54, 56, 57]
# item_to_check = 31
# print("element is present" if item_to_check in list1 else "element is not present")

# 8. Find the index of the first occurrence of an element in a list.
# list1 = [1, 2, 3, 54, 56, 57, 1]
# item_to_check = 3
# index = None
# counter = -1
# for item in list1:
#     counter += 1
#     if item_to_check == item:
#         index = counter
#         break
# print(f"{item_to_check} is present at index {index}")

# 9. Count the occurrences of an element in a list.
# list1 = [1, 2, 3, 54, 56, 57, 1]
# item_to_check = 1
# counter = 0
# for item in list1:
#     if item_to_check == item:
#         counter += 1
# print(f"{item_to_check} is present {counter} number of times in {list1}")

# 10. Reverse the order of elements in a list.
# list1 = [1, 2, 3, 54, 56, 57]
# print(f"reverse of {list1} is {list1[::-1]}")

# 11. Sort a list in ascending order.
# list1 = [54, 56, 57, 1, 2, 3]
# print(f"original list {list1}")
# list1.sort(key=None)
# print(f"Sorted list in ascending order {list1}")

# 12. Sort a list in descending order.
# list1 = [1, 2, 3, 54, 56, 57]
# print(f"original list {list1}")
# list1.sort(key=None, reverse=True)
# print(f"Sorted list in descending order {list1}")

# 13. Create a list of even numbers from 1 to 20.
# list1 = [item for item in range(1, 21) if item % 2 == 0]
# print(f"even numbers from 1 to 20 list {list1}")

# 14. Create a list of odd numbers from 1 to 20.
# list1 = [item for item in range(1, 21) if item % 2 != 0]
# print(f"odd numbers from 1 to 20 list {list1}")

# 15. Find the sum of all elements in a list.
# list1 = [1, 2, 3, 5, 6, 7]
# print(sum(list1))

# 16. Find the maximum value in a list.
# list1 = [1, 2, 3, 5, 6, 7]
# print(max(list1))

# 17. Find the minimum value in a list.
# list1 = [1, 2, 3, 5, 6, 7]
# print(min(list1))

# 18. Create a list of squares of numbers from 1 to 10.
# list1 = [num ** 2 for num in range(1, 11)]
# print(list1)

# 19. Create a list of random numbers.
# import random
# random_numbers = [random.randint(1, 100) for _ in range(10)]
# print(random_numbers)

# 20. Remove duplicates from a list.
# list1 = [1, 2, 3, 54, 56, 57, 1]
# print(f"unique item list {set(list1)}")

# 21. Find the common elements between two lists.
# list1 = [1, 2, 3, 54, 56, 57, 1]
# list2 = [54, 56, 57, 1]
# common_list = set([item for item in list1 if item in list2])
# print(f"common item list {common_list}")

# 22. Find the difference between two lists.
# list1 = [1, 2, 3, 54, 56, 57, 1]
# list2 = [54, 56, 57, 1]
# difference_list = set([item for item in list1 if item not in list2])
# print(f"common item list {difference_list}")

# 23. Merge two lists.
# list1 = [1, 2, 3, 54, 56, 57, 1]
# list2 = [64, 66, 67, 61]
# list1.extend(list2)
# print(f"common item  list {list1}")

#  24. Multiply all elements in a list by 2.
# list1 = [1, 2, 3, 5, 6, 7]
# updated_list = [item*2 for item in list1]
# print(updated_list)

# 25. Filter out all even numbers from a list.
# list1 = [1, 2, 3, 5, 6, 7]
# even_item_list = [item for item in list1 if item % 2 == 0]
# print(even_item_list)

# 26. Convert a list of strings to a list of integers.
# list_of_string = ['1', '2', '3', '5', '6', '7', 'a']
# list_of_int = [int(item) for item in list_of_string if item.isdigit()]
# print(f"final list is{list_of_int}")

# 27. Convert a list of integers to a list of strings.
# list_of_int = [1, 2, 3, 5, 6, 7]
# list_of_string = [str(item) for item in list_of_int]
# print(f"final list is{list_of_string}")


# 28. Flatten a nested list.
# nested_list = [['1', '2', '3', '5', '6', '7'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']]
# flatten_list = [item for sub_list in nested_list for item in sub_list]
# # for sub_list in nested_list:
# #     for item in sub_list:
# #         flatten_list.append(item)
# print(flatten_list)

# 29. Create a list of the first 10 Fibonacci numbers.
# fibonacci_numbers = [0, 1]
# for _ in range(2, 11):
#     next_num = fibonacci_numbers[-1] + fibonacci_numbers[-2]
#     fibonacci_numbers.append(next_num)
# print(fibonacci_numbers)

# 30. Check if a list is sorted.
# def is_sorted(lst):
#     return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
#
# sorted_list = [1, 2, 3, 4, 5]
# unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6]
#
# print(is_sorted(sorted_list))
# print(is_sorted(unsorted_list))

# 31. Rotate a list to the left by `n` positions.

# def rotate_left(lst, n):
#     n = n % len(lst)  # Ensure n is within the length of the list
#     return lst[n:] + lst[:n]
#
# # Example usage
# my_list = [1, 2, 3, 4, 5]
#
# rotated_list = rotate_left(my_list, 2)
# print(rotated_list)

# 32. Rotate a list to the right by `n` positions.
# def rotate_right(lst, n):
#     n = n % len(lst)  # Ensure n is within the length of the list
#     return lst[-n:] + lst[:-n]
#
# # Example usage
# my_list = [1, 2, 3, 4, 5]
#
# rotated_list = rotate_right(my_list, 2)
# print(rotated_list)

# 33. Create a list of prime numbers up to 50.
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# # Generate a list of prime numbers up to 50
# prime_numbers = [num for num in range(2, 51) if is_prime(num)]
#
# print(prime_numbers)

# 34. Split a list into chunks of size `n`.

# def chunk_list(input_list, chunk_size):
#     return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]
#     # chunked_list = []
#     # for i in range(0, len(input_list), chunk_size):
#     #     chunked_list.append(input_list[i:i + chunk_size])
#     # return  chunked_list
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# chunked_list = chunk_list(my_list, 3)
# print(chunked_list)

# 35. Find the second-largest number in a list.
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # removing the max and then calculating max
# my_list.remove(max(my_list))
# print(max(my_list))

# 36. Replace every element in a list with its square.
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # for x in range(0, len(my_list)):
# #     my_list[x] = my_list[x]**2
# print(my_list)
# my_list = [my_list[x]**2 for x in range(0, len(my_list))]
# print(my_list)

# 37. Convert a list to a dictionary where list elements become keys and their indices become values.
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result_disc = {}
# for index in range(0, len(my_list)):
#     result_disc.update({my_list[index]: index})
# print(result_disc)

# 38. Shuffle the elements of a list randomly.
# import random
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# random.shuffle(my_list)
# print(my_list)

# 39. Create a list of the first 10 factorial numbers.
# Function to calculate factorial
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)
#
# # Generate a list of the first 10 factorial numbers
# factorial_numbers = [factorial(i) for i in range(10)]
#
# print(factorial_numbers)

# 40. Check if two lists have at least one element in common.
# def check_common_element(lst1, lst2):
#     common_list = [item for item in lst1 if item in lst2]
#     return True if len(common_list) > 0 else False
#
# list1 = [1, 2, 3, 54, 56, 57, 1]
# list2 = [33, 1]
#
# print(check_common_element(list1, list2))

# 41. Remove all elements from a list.
# list1 = [1, 2, 3, 54, 56, 57, 1]
# print(f"before clearing {list1}")
# list1.clear()
# print(f"after clearing {list1}")

# 42. Replace negative numbers in a list with 0.
# list1 = [1, 2, 3, 54, 56, 57, 1, -3]
# print(f"before replacing {list1}")
# list1 = [num if num == abs(num) else 0 for num in list1]
# print(f"after replacing {list1}")

# 43. Convert a string into a list of words.
# string = "Convert a string into a list of words"
# print(string)
# print(string.split())

# 44. Convert a list of words into a string.
# list_of_words = ['Convert', 'a', 'string', 'into', 'a', 'list', 'of', 'words']
# string = " ".join(list_of_words)
# print(string)

# 45. Create a list of the first `n` powers of 2.
# my_list = [2 ** num for num in range(1, 11)]
# print(my_list)

# 46. Find the longest string in a list of strings.
# string_list = ["apple", "banana", "kiwi", "strawberry", "orange"]
# longest_string = max(string_list, key=len)
# print("Longest string:", longest_string)

# 47. Find the shortest string in a list of strings.
# string_list = ["apple", "banana", "kiwi", "strawberry", "orange"]
# shortest_string = min(string_list, key=len)
# print("Shortest string:", shortest_string)

# 48. Create a list of the first `n` triangular numbers.
# n = 10
# triangular_numbers = [i * (i + 1) // 2 for i in range(1, n + 1)]
# print(triangular_numbers)

# 49. Check if a list contains another list as a subsequence.
# def is_subsequence(sublist, mainlist):
#     sub_len = len(sublist)
#     temp_list = [x for x in mainlist if x in sublist]
#     return len(temp_list) == sub_len
#
# main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sub_list = [3, 5, 7, 61]
#
# result = is_subsequence(sub_list, main_list)
#
# print(result)

# 50. Swap two elements in a list by their indices.
# def swap_elements(lst, index1, index2):
#     lst[index1], lst[index2] = lst[index2], lst[index1]
#
# my_list = [1, 2, 3, 4, 5]
# print(f"before swapping {my_list}")
# # Swap elements at indices 1 and 3
# index1, index2 = 1, 3
# swap_elements(my_list, index1, index2)
#
# print(f"after swapping of index {index1} and {index2} {my_list}")


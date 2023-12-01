# 1. Given an array, check if it contains any duplicates or not.
# def duplicate_check(array):
#     if len(arr) == len(set(arr)):
#         #print("array does not have duplicate items")
#         return False
#     else:
#         #print("array does have duplicate items")
#         return True
# arr = [1, 2, 4, 2, 5, 9]
# print(duplicate_check(arr))


# 2. Given an array and an integer k, rotate the array to the right by k steps.
# arr = [1, 2, 3, 4, 5, 6, 7]
# k = 3
# # Output = [5, 6, 7, 1, 2, 3, 4]
# output = arr[-k:]+arr[:-k]
# print(output)

# 3. Reverse the given array in-place, means without using any extra data structure.
# arr = [2, 4, 5, 7, 9, 12]
# print(arr)
# print(f"memory address before reverse:{id(arr)}")
# arr.reverse()
# print(arr)
# print(f"memory address after reverse:{id(arr)}")


# 4. Given an array of integers, find the maximum element in an array
# arr = [10, 5, 20, 8, 15]
# output = max(arr)
# print(f"max element is the list {arr} is {output}")

# 5. Given a sorted array, remove the duplicate element without using any extra data structure.
# def remove_duplicates(arr):
#     print("memory address in function", id(arr))
#     if not arr:
#         return 0
#     unique_item = ""
#     for i in arr[::]:
#         if i == unique_item:
#             arr.remove(i)
#         else:
#             unique_item = i
#     return arr
#
# arr = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5]
# print("memory address at start ", id(arr))
# print("Array with duplicates:", arr)
# arr = remove_duplicates(arr)
# print("memory address at end ", id(arr))
# print("Array with duplicates removed:", arr)

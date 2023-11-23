# Recursive Python function to solve the tower of hanoi

# Recursive Python function to solve the tower of hanoi

# def TowerOfHanoi(n, source, destination, auxiliary):
#     if n == 1:
#         print("Move disk 1 from rod", source, "to rod", destination)
#         return
#     TowerOfHanoi(n - 1, source, auxiliary, destination)
#     print("Move disk", n, "from rod", source, "to rod", destination)
#     TowerOfHanoi(n - 1, auxiliary, destination, source)
#
#
# # Driver code
# n = 3
# TowerOfHanoi(n, 'A', 'C', 'B')
# A, C, B are the name of rods


# Recursive Relation of above program :
# T(n) = 2T(n-1) + 1     ——-equation-1
#
# Solving it by Substitution:
# T(n-1) = 2T(n-2) + 1     ———–equation-2
# T(n-2) = 2T(n-3) + 1     ———–equation-3
#
# Put the value of T(n-2) in the equation–2 with help of equation-3
# T(n-1)= 2( 2T(n-3) + 1 ) + 1     ——equation-4
#
# Put the value of T(n-1) in equation-1 with help of equation-4
# T(n)= 2( 2( 2T(n-3) + 1 ) + 1 ) + 1
# T(n) = 2^3 T(n-3) + 2^2 + 2^1 + 1
#
# After K times :
# T(n)= 2^k T(n-k) + 2^{(k-1)} + 2^{(k-2)} + ............ +2^2 + 2^1 + 1
#
# Base condition T(1) =1
# n – k = 1
# k = n-1
# put, k = n-1
# T(n) =2^{(n-1)}T(1) + + 2^{(n-2)} + ............ +2^2 +2^1 + 1
#
# It is a GP series, and the sum is 2^n - 1
#
# T(n)= O(2^n - 1), or  O(2^n)   which is exponential

# Q. 3 Print the max value of the array [ 13, 1, -3, 22, 5].

# arr = [13, 1, -3, 22, 5]
# print(f"max value in array {arr} is {max(arr)}")

# Q.4 Find the sum of the values of the array [92, 23, 15, -20, 10].

# arr = [92, 23, 15, -20, 10]
# print(f"sum of the values of array {arr} is {sum(arr)}")


# Q.5 Given a number n. Print if it is an armstrong number or not.An armstrong number is a number if the sum
# of every digit in that number raised to the power of total digits in that number is equal to the number.
# Example : 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 hence 153 is an armstrong number. (Easy)
# Input1 : 153
# Output1 : Yes
# Input 2 : 134
# Output2 : No

# def check_armstrong_num(num_to_check, exponent):
#     if num_to_check // 10 == 0:
#         return pow((num_to_check % 10), exponent)
#     else:
#         return pow((num_to_check % 10), exponent) + check_armstrong_num(num_to_check // 10, exponent)
#
#
# nums = [153, 134, 370, 371, 407, 1634, 8208, 9474, 48834, 548834]
# for num in nums:
#     result = check_armstrong_num(num, len(str(num)))
#     # print(result)
#     print(f"\n number {num} is armstrong number" if num == result else f"\n number {num} is not armstrong number")
#
# # time complexity of above is O(log n base 10)

# Q.2 Given two strings word1 and word2, return the minimum number of operations required to convert word1
# to word2.
def min_distance(word1, word2):
    m, n = len(word1), len(word2)
    # print(m,n)

    # Create a 2D array to store the minimum edit distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # print(dp)

    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    # print(dp)
    # Fill in the rest of the array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],        # Deletion
                                  dp[i][j - 1],        # Insertion
                                  dp[i - 1][j - 1])    # Substitution

    return dp[m][n]

# Example 1
word1 = "horse"
word2 = "ros"
result = min_distance(word1, word2)
print(f"The minimum number of operations to convert '{word1}' to '{word2}' is: {result}")

# Example 2:
word1 = "intention"
word2 = "execution"
result = min_distance(word1, word2)
print(f"The minimum number of operations to convert '{word1}' to '{word2}' is: {result}")
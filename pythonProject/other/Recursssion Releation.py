# 1. Find the value of T(2) for the recurrence relation T(n) = 3T(n-1) + 12n, given that T(0)=5.
# T(n) = 3T(n-1) + 12n # recurrence relation
# T(0) = 5 # given
# # Equation 1 for n = 1
# T(1)=3T(1-1)+12*1
# T(1)=3T(0)+12*1
# T(1)=3*5 + 12 # Replacing T(0) with 5 as T(0) = 5
# T(1)=15 + 12
# T(1)= 27
# # Equation 2 for n= 2
# T(2)=3T(2-1)+12*2
# T(2)=3T(1)+24 # T(1)= 27 from above
# T(2)=3*27+24
# T(2)=81+24
# T(2)=105

# 2. Given a recurrence relation, solve it using the substitution method:
# a. T(n) = T(n-1) + c the time complexity will be O(n) below is the steps
# taking base case n = 1 return 1
# get the value of T(n-1) ,T(n-2), T(n-3) by replacing values in the above relation
# T(n-1) = T(n-1-1)+c = T(n-2)+c
# T(n-2) = T(n-2-1)+c = T(n-3)+c
# T(n-3) = T(n-3-1)+c = T(n-4)+c
#
#
# # start replacing the values in the main equation
# T(n) = T(n-1) + c
#     # replace T(n-1) from above
#     =T(n-2)+c +c = T(n-2)+2c
#     # replace T(n-2) from above
#     =T(n-3)+c + 2c = T(n-3)+3c
#     # replace T(n-3) from above
#     =T(n-4)+c + 3c = T(n-4)+4c
# # assuming after K steps
#     =T(n-K)+Kc # main equation
# # Keeping base case in mind
# n-K=1
# K=n-1
# # replacing the value of k in main equation
# T(n) = T(n-n-1) + (n-1)*c
#     =T(1)+c*n-c
#     =1+c*n-c # c is constant
# # the biggest impacting factor is n Hence Time complexity will be
# O(n)

# 2. Given a recurrence relation, solve it using the substitution method:
# b. T(n) = 2T(n/2) + n O(n*logn with base 2)

# T(n) = 2T(n/2) + n # EQ1
# # get the value of T(n/2)
# T(n/2)=2T(n/2^2) + n/2
# # replacing the value of T(n/2) in EQ1
# T(n)=2(2T(n/2^2) + n/2) +n = 2^2T(n/2^2)+n+n # EQ2
# # get the value of T(n/2^2)
# T(n/2^2) = 2T(n/2^3) + n/2^2
# # replacing the value of T(n/2^2) in EQ2
# T(n)=2^2(2T(n/2^3) + n/2^2)+n+n = 2^3T(n/2^3)+n+n+n # EQ3
#
# # after k steps
# =2^k(n/2^k)+k*n  # EQ4
# # keeping base case
# n/2^k = 1
# n = 2^k --- a
# #taking log with base 2
# k = log n base 2 ---b
# # putting the value of K in EQ4
# =2^k(n/2^k)+k*n
# # using a and b mentioned below
# =n(1)+n*log n base 2
# =n+n*logn
# # # the biggest impacting factor is n Hence Time complexity will be
# # O(n)
# so the time complexity of above equation would be "O(n*logn)"

# 2. Given a recurrence relation, solve it using the substitution method:
# c. T(n) = 2T(n/2) + c time complexity will be O(n)
# T(n) = 2T(n/2) + c
# = 2(2T(n/2^2)+c+c
# = 2^2(T(n/2^2))+2c #--- EQ2
# =2^2(2T(n/2^3))+3c
# =2^3(T(n/2^3))+3c
#
# #  after K steps
# =2^kT(n/2^k)+k*c
#
# # for the base case
# n/2^k = 1
# n = 2^k or 2^k = n
# k = log n with base2
# # for the base case
# T(n) = nT(1)+log n*c
#  = n+ logn*c
# # the biggest impacting factor is n Hence Time complexity will be
# O(n)

# 2. Given a recurrence relation, solve it using the substitution method:
# d. T(n) = T(n/2) + c time complexity will be O(log n)
# T(n)
# =T(n/2) + c #--- EQ1
# =T(n/2^2)+2c
# =T(n/2^2)+2c #--- EQ2
# =T(n/2^3)+3c #--- EQ3

#
# #  after K steps
# =T(n/2^k)+k*c
#
# # for the base case
# n/2^k = 1
# n = 2^k or 2^k = n
# k = log n with base2
# # for the base case
# T(n) = T(1)+log n*c
#  = 1+ log n*c
# # the biggest impacting factor is n Hence Time complexity will be
# O(log n)

# 3. Given a recurrence relation, solve it using the recursive tree approach:
# a. T(n) = 2T(n-1) +1
# as this is a recursive tree approach I am not able to draw a tree here.
# but the calculation will be as per GP series formula
Time complexity for above will be O(2^n) i.e. exponential complexity


# 3. Given a recurrence relation, solve it using the recursive tree approach:
# b.T(n) = 2T(n/2) + n
Time complexity for above will be O(nlogn) i.e.exponential complexity
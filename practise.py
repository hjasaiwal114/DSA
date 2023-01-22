# checking for unique 
# arr  = [2,3,3,4,2,6,4]

# def ans(arr):
#     Unique = 0
#     for i in arr:
#         Unique ^= i
    
#     return Unique
# print(ans(arr))

#checking for unique number
# arr = []
# n = 5
# ans = 0
# base = 5
# while n>0:
#     last = n & 1
#     n = n >> 1
#     ans += last * base
#     base = base*5

# import math
# n = 10
# b = 2

# ans = math.log(n) / math.log(b) +1
# print(ans)
# n = 31

# ans = bool((n & (n-1)) == 0)
# print(ans)

# base  = 3
# power = 6
# ans = 1
# while power > 0:
#     if power & 1 == 1:
#         ans *= base
#     base *= base
#     power = power >> 1
# print(ans)

# bin(n):
#     count = 0 
#     while n > 0:
#         count += 1
#         n = n & (n-1) 
#     return count




# def fact(n):
#     if n == 0:
#         return 1

#     fnm1 = int(fact(n-1))
#     fn = int(n*fact(n-1))
#     return fn
# print(fact(5))


# def sum(n):
#     if n ==1:
#         return 1

#     snm1 = sum(n-1)
#     sn = n + snm1
#     return sn
# print(sum(5))


# def fib(n):
#     if n == 0 or n ==1:
#         return n

#     fnm1 = fib(n-1)
#     fnm2 = fib(n-2)
#     fn =  fnm1 + fnm2
#     return fn 
# print(fib(25))

# def  isSorted(arr, i):
#     if i == len(arr)-1:
#         return True
#     if arr[i] > arr[i+1]:
#         return False
#     return isSorted(arr ,i+1)

# arr = [1,2,0,4]
# print(isSorted(arr ,0))

# def firstOccurence(arr,key,i):
#     if i == len(arr):
#         return -1
#     if arr[i] == key:
#         return i  
#     return firstOccurence(arr , key, i+1)
# arr = [8,3,6,9,5,10,2,5,3]
# print(firstOccurence(arr,5,0))


# def power(x,n):
#     if n == 0:
#         return 1
#     xnm1 = power(x,n-1)
#     xn = x* xnm1
#     return xn
# print(power(2,10))

# def optimizedPower(a,n):
#     if n == 0:
#         return 1
#     halfpowerSq = optimizedPower(a,n//2) 
#     halfpowerSq = halfpowerSq*halfpowerSq
#     # n is odd
#     if n%2 != 0:
#         halfpowerSq = a*halfpowerSq
#     return halfpowerSq
# print(optimizedPower(2,10))

# def tillingProblem(n): # 2 * n (floor size)
#     # base case
#     if n ==0 or n==1 :
#         return 1

#     # kaam
#     # vertical choice

#     # vertical choice
#     fnm1 = tillingProblem(n-1)
#     # hoizontal choice
#     fnm2 = tillingProblem(n-2)

#     totways = fnm1 + fnm2
#     return totways
# print(tillingProblem(4))

# def removeDuplicates(str, idx , newStr , map):
#     if idx == len(str):
#         print(newStr)
#     # kaam
#     currChar = str[idx]
#     if currChar in map :
#         # duplicate
#         removeDuplicates(str,idx+1,newStr,map)
#     else:
#         removeDuplicates(str ,idx+1, newStr.append(currChar), map)

# print(removeDuplicates("appppnnacollege",0," ",[26] ))  # na bhai na ye question ek bar python m delh lio


def  friendsparing(n):
    if n ==1 or n ==2 :
        return n
    #choice
    #single
    fnm1 = friendsparing(n-1)

    #pair
    fnm2 = friendsparing(n-2)
    pairwaWays = (n-1)*fnm2

    #toWays
    totways = fnm1 + pairwaWays
    return totways
print(friendsparing(3))
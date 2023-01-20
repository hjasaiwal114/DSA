
# def print2largest(arr, n):
#     # code here
#     mx = 0
#     secondmx = -1
#     for i in arr:
#         mx = max(mx, i)
#     for i in arr:
#         if i == mx:
#             continue
#         secondmx = max(i, secondmx)
#     return secondmx
# arr = [1,22,34,12,45,7]
# print(print2largest(arr = [1,22,34,12,45,7], n = 6))

def findzero(arr , n , m ):
    i = 0
    j = 0
    while i <n:
        if arr[i] == 0:
            m -= 1
        if m <0 :
            if arr[j] == 0:
                m += 1

            j += 1
        i += 1
    return i - j

print(findzero(arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1], n =11, m =2 ))

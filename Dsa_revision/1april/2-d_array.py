from array import *

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Original Array")
for _ in arr:
    for i in _:
        print(i, end=" ")
    print()

arr.insert(2, [11, 12, 13])

print("Modified Array")
for _ in arr:
    for i in _:
        print(i, end=" ")
    print()
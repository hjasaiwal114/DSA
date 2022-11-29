# # stack data structure 
# # using list
# stack = []
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack)
# print(stack.pop())

# top = stack[-1]
# print(top)
# size = len(stack)
# print(size)

# from  _collections import deque
# stack = deque()
# stack.apppend(10)
# stack.apppend(20)
# stack.apppend(30)
# print(stack.pop())
# top = stack[-1]
# print(top)
# size = len(stack)
# print(size)



# import math
# class Node:
#     def __init__(self,d):
#         self.data = d
#         self.next = None
# class MyStack:
#     def __init__(self):
#         self.head = None
#         self.sz = 0
#     def push(self, x):
#         temp = Node(x)
#         temp.next = self.head
#         self.head = temp
#         self.sz = self.sz+1
#     def size(self):
#         return self.sz
#     def peek(self):
#         if self.head == None:
#             return math.inf
#         return self.head.data
#     def pop(self):
#         if self.head == None:
#             return math.inf
#         res = self.head.data
#         self.head = self.head.next
#         self.sz = self.sz - 1
#         return res
# s = MyStack()
# s.push(10)
# s.push(20)
# s.push(30)
# print(s.pop())
# print(s.peek())
# pr  int(s.size())


def ismatching(a,b):
    if( a =='(' and b == ')') or \
       (a == '{' and b == '}') or \
       (a == '[' and b == ']') :
        return True
    else:
        return False
def isBalances(exper):
    stack = []
    for x in exper:
        if x in ('(', '{' , '['):
            stack.append(x)
        else:
            if not stack:
                return False
            elif ismatching(stack[-1], x) == False:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True

a = input()
print(isBalances(a))

a = input()
print(isBalances(a))












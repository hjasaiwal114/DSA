# class Node:
#     def __init__(self,k):
#         self.key = k
#         self.next = None

# temp1 = Node(10)
# temp2 = Node(20)
# temp3 = Node(30)
# temp4 = Node(40)

# temp1.next = temp2
# temp2.next = temp3
# temp3.next = temp4

# head = temp1
# print(head.key)
# print(head.next.key)
# print(head.next.next.key)
# print(head.next.next.next.key)

# class Node:
#     def __init__(self,key):
#         self.key = key
#         self.next = None
# def printList(head):
#     curr = head
#     while curr != None:
#         print(curr.key,end =" ")
#         curr = curr.next

# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(15)
# head.next.next.next = Node(30)
# printList(head)  


class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
def search(head,x):
    pos = 1
    curr = head
    while curr!= None:
        if curr.Key == x:
            return pos
        pos = pos + 1
        curr = curr.next
    return -1

head = Node(10)
head.next = Node(15)
head.next.next = Node(20)
head.next.next.next = Node(25)
x = 20
print(search(head, x))

# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.next = None


# def search(head, x):
#     pos = 1
#     curr = head
#     while curr != None:
#         if curr.key == x:
#             return pos
#         pos = pos + 1
#         curr = curr.next
#     return -1


# head = Node(10)
# head.next = Node(15)
# head.next.next = Node(20)
# head.next.next.next = Node(25)
# x = 20
# print(search(head, x))
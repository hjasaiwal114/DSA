# making of doubouly lined list

# class node:
#     def __init__(self,data):
#         self.data = data
#         self.prev = None
#         self.next = None
# def double_linked(head):
#     curr = head
#     while curr:
#         print(curr.data, end=" ")
#         curr = curr.next
#     print()
# head = node(10)
# temp1 = node(20)
# temp2 = node(30)
# temp3 = node(40)
# temp4 = node(50)
# head.next = temp1
# temp1.prev = head

# temp1.next = temp2
# temp2.prev  = temp1

# temp2.next = temp3
# temp3.prev = temp2

# temp3.next= temp4
# temp4.prev = temp3

# double_linked(head)

# insert at the bedinning of DLL in python

# class Node:
#     def __init__(self,k):
#         self.key = k
#         self.prev = None
#         self.next = None

# def insertBegin(head, x):
#     temp =Node(x)
#     if head != None:
#         head.prev = temp
#     temp.next = head
#     return temp





# def printList(head):
#     curr = head
#     while curr != None:
#         print(curr.key , end =" ")
#         curr = curr.next
# head = None
# head = insertBegin(head, 10)
# head = insertBegin(head,20)
# printList(head)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# def insertEnd(head ,x):
#     temp = Node(x)

#     if head == None:
#         return temp
    
#     else:

#         curr = head
#         while curr.next!=None:
#             curr = curr.next
#         curr.next = temp
#         temp.prev = curr

#         return head
# def printDll(head):
#     curr = head
#     while curr != None:
#         print(curr.data, end=" ")
#         curr = curr.next
#     print()

# head =Node(10)
# temp1 =Node(20)
# temp2 = Node(30)

# head.next = temp1
# temp1.prev = head

# temp1.next = temp2
# temp2.prev = temp1


# head = insertEnd(head, 40)

# printDll(head)

# class Node:
#     def __init__(self , data):
#         self.data = data
#         self.next = None
#         self.prev = None

# def delhead(head):
#     if head == None:
#         return None
#     if head.next == None:
#         return None
#     else:
#         head.next = head.next
#         head.prev = None
#         return head

# def printDll(head):
#     curr = head
#     while curr:
#         print(curr.data , end =" ")
#         curr = curr.next
#     print()

# head =Node(10)
# temp1 =Node(20)
# temp2 = Node(30)

# head.next = temp1
# temp1.prev = head

# temp1.next = temp2
# temp2.prev = temp1

# printDll(head)

# head = delhead(head)

# printDll(head)



# ONLY FUNCTION ALL OF THE CODE IS SAME

# def delLadt(head):
#     if head == head:
#         return None
#     if head.next == None:
#         return None
#     curr = head
#     while curr.next.next != None:
#         curr = curr.next
#     curr.next = None
#     return head

#  REVERSE LINKED LIST
# def revdll(head):
#     if head == None:
#         return None
#     if head.next == None:
#         return None
#     curr = head
#     prev = None
#     while curr:
#         prev = curr
#         curr.next , curr.prev = curr.prev, curr.next
#         curr = curr.prev
#     return prev
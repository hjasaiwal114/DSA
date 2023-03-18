class Node:
    
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):

        # Empty Linked List
        self.head = None
        self.n = 0

def __len__(self):
    return self.n

def insert_head(self, values):

    # new node
    new_node = Node(values)

    # creating connection
    new_node.next = self.head

    # reassign head
    self.head = new_node

    # increment n
    self.n = self.n + 1
 def __str__(self):

    curr = self.head
    result  = ''

    while curr != None:
        result = result + str(curr.data) + " ->"
        print(curr.data)
        curr = curr.next

    return result[:-2]

def insert_after(self, after ,value):
    new_node = Node(value)

    curr =  self.head
    while curr != None:
        if curr.data == after:
            break
        curr = curr.next

    # case 1 break -> item apko mil gaya -> curr -> not none
    if curr != None:
        # logic
        new_node.next = curr.next 
        curr.next = new_node
    else:
        return "Item not found"
    

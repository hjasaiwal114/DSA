class Node:

    def __init__(self,value):
        self.data = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None
    
    def isempty(self):
        return self.top == None
    
    def push(self, value):

        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
    def peek(self):
        if(self.isempty()):
            return "Stack Empty"
        else:
            return self.top.data


    def travese(self):

        temp = self.top
        while temp != None:
            print(temp.data)
            temp = temp.next

    def reverse_string(text):

        s = stack()
        for i in text:
            s.push(i)

        res = ""

        while (not s.empty()):
            res = res + s.pop()
        print(res)
        
    def text_editor(text, pattern):

        u = stack()
        r = stack()

        for i in text:
            u.push(i)
        
        for i in pattern:

            if i == 'u':
                data = u.pop()
                r.push(data)
            else:
                data = r.pop()
                u.push(data)

        res = " "

        while(not u.is_empty()):
            res = u.pop() + res

        print(res)


    def find_the_celeb(L):
        s = Stack()

        for i in range(len(L)):
            s.push(i)

        while s.size() >= 2:

            i = s.pop()
            j = s.pop()

            if L[i][j] == 0:
                # j is not a celebrity
                s.push(j)

            else:
                # i is not a celeb
                s.push(j)
        celeb  = s.pop()

        for i in range(len(L)):

            if i != celeb:
                if L[i][celeb] == 0 or L[celeb][i] == 1:
                    print("No one is a celebrety")
                    return

            print("The celebrity is", celeb)


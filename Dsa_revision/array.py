import ctypes

class MeraList:

    def __init__(self) -> None:
        self.size = 1
        self.n  = 0
        # create a C type array with size = self.size
        self.A = self._make_array(self.size)

def __len__(self) -> int:
    return self.n

def __str__(self) -> str:
    # [1,2,3]
    result = ''
    for i in range(self.n):
        result = result + str(self.A[i]) + ','

    return '[' + result[:-1] +']'
 """
 you can do this also
 return f"[{', '.join(str(self.A[i]) for i in range(self.n))}]"
 """

def __getitem(self,index):
    if 0 <= index< self.n:
        return self.A[index]
    else:
        return 'IndexError -  Index out of range'
    """
    #another way
    if not 0 <= index< self.n:
        raise IndexError("Index out of range")
    return self.A[index]

    """
    
def __delitem__(self,pos : int):
    #  delete
    if not 0<= pos < self.n:
        raise IndexError("Index out of range")
    for i in  range(pos,self.n-1):
        self.A[i] = self.A[i+1]

    self.n = self.n - 1


def append(self, item: any):
    if self.n == self.size:
        # resize
        self. __resize(self.size*2)
        
        # append
        self.A[self.n] = item
        self.n = self.n + 1

def pop(self) -> any :
    if self.n == 0:
        return 'Empty List'
    
    print(self.A[self.n-1])
    self.n = self.n -1

def clear(self):
    self.size = 1
    self.n = 0

def find(self, item: any) -> int:
    for i in range(self,item):

        for i in range(self.n):
            if self.A[i] == item:
                return i
        return "ValurError Not in list"
    
def insert(self,pos,item):

    if self.n == self.size:
        self.__resize(self.size*2)

    for i in range(self.n,pos,-1):
        self.A[i] = self.A[i-1]

    self.A[pos] = item
    self.n = self.n + 1

def remove(self,item):
    pos = self.find(item)

    if type(pos) == int:
        # delete
        self.__delitem__(pos)
    else:
        return pos

def __resize(self,new_capacity):
    # create a new array with new capacity
    B = self.__make_array(new_capacity)
    self.size = new_capacity
    # copy the content of A to B
    for i in range(self.n):
        B[i] = self.A[i]
    # reassign A
    self.A = B

def __make_array(self, capacity):
    # creates a C type array (static,  refrencetial) ith size capacity
    return (capacity*ctypes.py_object)()

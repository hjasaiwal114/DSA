class MeraList:

    def __init__(self):
        self.size = 1
        self.n  = 0
        # create a C type array with size = self.size
        self.A = self._make_array(self.size)

    def __make_array(self, capacity):
        # creates a C type array (static,  refrencetial) ith size capacity
        return (capacity*ctypes.py_object)()

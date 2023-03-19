class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def _linear_probe(self, index):
        return (index + 1) % self.size

    def put(self, key, value):
        hash_value = self._hash_function(key)
        if self.keys[hash_value] is None:
            self.keys[hash_value] = key
            self.values[hash_value] = value
        else:
            index = self._linear_probe(hash_value)
            while self.keys[index] is not None and self.keys[index] != key:
                index = self._linear_probe(index)
            if self.keys[index] == key:
                self.values[index] = value
            else:
                self.keys[index] = key
                self.values[index] = value

    def get(self, key):
        hash_value = self._hash_function(key)
        if self.keys[hash_value] == key:
            return self.values[hash_value]
        else:
            index = self._linear_probe(hash_value)
            while self.keys[index] is not None and self.keys[index] != key:
                index = self._linear_probe(index)
            if self.keys[index] == key:
                return self.values[index]
            else:
                return None

    def delete(self, key):
        hash_value = self._hash_function(key)
        if self.keys[hash_value] == key:
            self.keys[hash_value] = None
            self.values[hash_value] = None
        else:
            index = self._linear_probe(hash_value)
            while self.keys[index] is not None and self.keys[index] != key:
                index = self._linear_probe(index)
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None

    def __str__(self):
        res = []
        for i in range(self.size):
            if self.keys[i] is not None:
                res.append(f"{self.keys[i]}: {self.values[i]}")
        return "{" + ", ".join(res) + "}"

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        hash_value = self._hash_function(key)
        slot = self.table[hash_value]
        for i, (k, v) in enumerate(slot):
            if k == key:
                slot[i] = (key, value)
                return
        slot.append((key, value))

    def get(self, key):
        hash_value = self._hash_function(key)
        slot = self.table[hash_value]
        for k, v in slot:
            if k == key:
                return v
        return None

    def delete(self, key):
        hash_value = self._hash_function(key)
        slot = self.table[hash_value]
        for i, (k, v) in enumerate(slot):
            if k == key:
                del slot[i]
                return

    def __str__(self):
        res = []
        for i, slot in enumerate(self.table):
            for k, v in slot:
                res.append(f"{k}: {v}")
        return "{" + ", ".join(res) + "}"

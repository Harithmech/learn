class hashing:
    def __init__(self, b):
        self.branch = b
        self.table = [[] for i in range(b)]

    def insert(self, ele):
        i = ele % self.branch
        self.table[i].append(ele)

    def delete(self, ele):
        i = ele % self.branch
        if ele in self.table[i]:
            self.table[i].remove(ele)

    def search(self, ele):
        i = ele % self.branch
        return ele in self.table[i]

    
ob = hashing(7)
ob.insert(70)
ob.insert(71)
ob.insert(9)
ob.insert(56)
ob.insert(72)
print(ob.search(9))
ob.delete(9)
print(ob.search(9))
ob.delete(100)

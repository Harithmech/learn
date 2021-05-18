class Myhash:
    def __init__(self, b):
        self.bucket = b
        self.table = [[] for x in range(b)]

    def insert(self, x):
        i = x % self.bucket
        self.table[i].append(x)

    def remove(self, x):
        i = x % self.bucket
        self.table[i].remove(x)

    def search(self, x):
        i = x % self.bucket
        return x in self.table[i]

ob = Myhash(7)
ob.insert(70)
ob.insert(71)
ob.insert(9)
ob.insert(56)
ob.insert(72)
print(ob.search(9))
ob.remove(9)
print(ob.search(9))

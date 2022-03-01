# From algomonster. Not by me.
class UnionFind:
    def __init__(self):
        self.f = {}

    def find(self, x):
        y = self.f.get(x, x)
        if y != x:
            self.f[x] = y = self.find(y)
        return y

    def union(self, x, y):
        self.f[self.find(x)] = self.find(y)

class Node:
    def __init__(self, val):
        self.val = val
        self.freq = 1
        self.children = {}

    def insert(self, s):
        self.insertHelper(s, 0)
        self.freq += 1

    def insertHelper(self, s, i):
        if i == len(s):
            return
        else:
            c = s[i]
            if c in self.children:
                node = self.children[c]
                node.insertHelper(s, i+1)
            else:
                node = Node(c)
                self.children[c] = node
                node.insertHelper(s, i+1)

    def contains(self, s):
        return self.containsHelper(s, 0)

    def containsHelper(self, s, i):
        if i == len(s):
            return True
        else:
            c = s[i]
            if c in self.children:
                node = self.children[c]
                return node.containsHelper(s, i+1)
            else:
                return False

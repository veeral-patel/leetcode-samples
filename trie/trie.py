class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}

    def insert(self, s):
        self.insertHelper(s, 0)

    def insertHelper(self, s, i):
        if i == len(s):
            return
        else:
            # if the character to insert is in the trie,
            # let's add the rest of the string under that node.
            if s[i] in self.children:
                node = self.children[s[i]]
                node.insertHelper(s, i+1)
            else:
                # otherwise, let's create a new node, then insert
                # the rest of the string under it
                node = Node(s[i])
                self.children[s[i]] = node
                node.insertHelper(s, i+1)

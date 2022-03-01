class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isWord = False

    def insert(self, s):
        self.insertHelper(s, 0)

    def insertHelper(self, s, i):
        if i == len(s):
            return

        c = s[i]
        self.children.setdefault(c, Node(c))
        self.children[c].insertHelper(s, i+1)

        if i == len(s)-1: # at last letter of word
            self.children[c].isWord = True

    def getWords(self):
        if not self.children:
            return [self.val]

        subWords = []
        for letter, child in self.children.items():
            childWords = child.getWords()
            for childWord in childWords:
                if self.val == "$":
                    subWords.append(childWord)
                else:
                    subWords.append(self.val + childWord)

        return subWords

def indexPairs(self, text, words):
    pass


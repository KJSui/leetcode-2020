class Solution:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        children = self.root
        for w in word:
            if w not in self.root:
                children[w] = {}
            children = children[w]
        children["#"] = "#"

    def search(self, word):
        children = self.root
        for i in word:
            if i not in children:
                return False
            children = children[i]

        return "#" in children

    def startWith(self, prefix):
        children = self.root
        for c in prefix:
            if c not in children:
                return False
            children = children[c]

        return True

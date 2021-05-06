class WorldNode(object):
    def __init__(self):
        self.children = dict()
        self.isLeaf = False 


class WorldDcitionary:
    def __init__(self):
        self.root = WorldNode()

    def addWord(self, word):
        self.addWordHelper(word, 0, self.root)

    def addWordHelper(self, word, index, parent):
        c = word[index]
        if c not in parent.children:
            parent.children[c] = WorldNode()
        if len(word) == index+1:
            parent.children[c].isLeaf = True 
            return 
        self.addWordHelper(word, index+1, parent.children[c])

    def search(self, word):
        return self.searchHelper(word, 0, self.root)

    def searchHelper(self, word, index, parent):
        if index == len(word):
            return parent.isLeaf
        c = word[index]
        if c is ".":
            for i in parent.children:
                if self.searchHelper(word, index+1, parent.children[i]):
                    return True 
            return False 
        elif c in parent.children:
            return self.searchHelper(word, index+1, parent.children[c])
        

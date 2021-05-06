class wordNode(object):
    def __init__(self):
        self.isLeft = True
        self.children = {}
class Solution:
    def __init__(self):
        self.root = wordNode()

    def addWord(self, word):
        rt = self.root
        for c in word:
            if c not in rt:
                rt.children[c] = wordNode()
            rt = rt.children[c]
        rt.isLeaf = True


    def search(self, word):
        return self.dfs(word, 0, self.root)

    def dfs(self, word, start, parent):
        if start == len(word):
            return parent.isLeaf

        c = word[start]
        if c is '.':
            for w in parent.children:
                if self.dfs(word, start+1, parent.children[w]):
                    return True
            return False
        elif c in parent.children:
            return self.dfs(word, start+1, parent.children[c])

        return False
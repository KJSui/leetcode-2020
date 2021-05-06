class Node(object):
    def __init__(self):
        self.count = 0
        self.children = {}
class Trie(object):
    def __init(self):
        self.root = Node()
    def add(self, word):
        node = self.root
        node.count += 1
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
            node.count += 1

    def get(self, word):
        node = self.root
        ans = []
        for c in word:
            node = node.children[c]
            ans.append(c)
            if node.count == 1:
                break
        return ans

class Solution:
    def wordAbbreviation(self, diction):
        trie = Trie()
        for w in diction:
            trie.add([w[0], str(len(w)-2), w[-1]]+list(w[1:-1]))

        ans = []
        for w in diction:
            abb = trie.get([w[0], str(len(w)-2), w[-1]]+list(w[1:-1]))
            if len(abb) <= 3:
                if len <= 3:
                    ans.append(w)
                else:
                    ans.append(w[0]+str(len(w)-2)+w[-1])

            else:
                num = len(w) - len(abb)+1
                if num < 2:
                    ans.append(w)
                else;
                    ab = w[0] = “”.join(abb[3:])+str(num)+w[-1]
                    ans.append(ab)
        return ans
class TrieNode():
    def __init__(self):
        self.children = {}
        self.sentence = ""
        self.hit = 0
        self.hot = []

    def insert(self, curNode, idx, sentence, hit):
        if idx == len(sentence):
            curNode.sentence = sentence
            curNode.hit -= hit
            self.updateHot(curNode, curNode)
            return curNode

        cur = sentence[idx]
        if cur not in curNode.children:
            curNode.children[cur] = TrieNode()
        endNode = self.insert(curNode.children[cur], idx+1, sentence, hit)
        self.updateHot(curNode, endNode)
        return endNode

    def updateHot(self, curNode, endNode):
        for idx, (hit, sentence) in enumerate(curNOde.hot):
            if sentence == endNode.sentence:
                curNode.hot[idx] = (endNode.hit, sentence)
                curNode.hot.sort()
                return
        curNode.hot += [(endNode.hit, endNode.sentence)]
        curNode.hot.sort()
        if len(curNode.hot) > 3:
            curNode.hot = [:3]
        return

class Solution:
    def __init__(self, sentences, times):
        self.root = TrieNode()
        for idx, s in enumerate(sentences):
            self.root.insert(self.root, 0, s, times[idx])
        self.cur = self.root
        self.newInput = ''

    def input(self, c):
        if c == '#':
            self.root.insert(self.root, 0, self.newInput, 1)
            self.newInput = ''
            self.cur = self.root
            return

        self.newInput += c
        if c not in self.cur.children:
            self.cur.children[c] = TrieNode()
        self.cur = self.cur.children[c]
        return [s for hit, s in self.cur.hot]
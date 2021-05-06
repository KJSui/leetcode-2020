class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.sentence = ''
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
        endNode =   self.insert(curNode.children[cur], idx+1, setntence, hit)
        self.updateHot(curNode, endNode)
        return endNode

    def updateHot(self, curNode, endNode):
        for idx, (hit, sentence) in enumerate(curNode.hot):
            if sentence == endNode.sentence:
                curNode.hot[idx] = (endNode.hit, sentence)
                curNode.hot.sort()
                return

        curNode.hot.append((endNode.hit, endNode.sentence))
        curNode.hot.sort()
        if len(curNOde.hot) > 3:
            curNode.hot = curNode.hot[:3]
        return
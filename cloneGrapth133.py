class Solution:
    def __init__(self):
        self.cp = {}

    def cloneGraph(self, node):
        if not node:
            return None
        newNode = UndirectedGraphNode(node.val)
        self.cp[node] = newNode
        if len(node.neighbors):
            for i in node.neighbors:
                if i in self.cp:
                    newNode.neightbors.append(self.copy[i])
                else:
                    newNode.neightbors.append(self.cloneGraph(i))
        return newNode

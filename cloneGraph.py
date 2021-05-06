class Solution:
    def __init__(self):
        self.copy = {}
    def cloneGraph(self, node):
        if not node:
            return None 
        newNode = Node(node.val)
        neight = []
        for i in neight:
            if i in self.copy:
                neight.append(self.copy[i])
            else:
                neight.append(self.cloneGraph(i))
        newNode.neighbors = neight

        return newNode

    
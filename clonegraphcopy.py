class GraphNode:
    def __init__(self, node, neigh):
        self.val = node
        self.neigh = neigh
class Solution:
    def __init__(self):
        self.clone = {}
    def cloneGraph(self, node):
        if not node:
            return None
        newNode = GraphNode(node, None)
        neigh = {}
        self.clone[node] = newNode
        if len(node.neigh):
            for nd in node.neigh:
                if nd not in self.clone:
                    neigh.append(self.cloneGraph(nd))
                else:
                    neigh.append(self.clone[nd])
        newNode.neigh = neigh
        return newNode
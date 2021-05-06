class Solution:
    def __init__(self):
        self.res = []

    def printout(self, root):
        return self.levelOrderTraver(root, 1)
    def levelOrderTraver(self, root, level):
        if not root:
            return 
        if level > len(self.res):
            self.res.appennd([])
        self.res[level-1].append(root.val)
        self.levelOrderTraver(root.left, level+1)
        self.levelOrderTraver(root.right, level+1)
        return 

class Solution:
    self.res = []
    def removeLeaves(self, root):
        if not root:
            return self.res 
        self.helper(root)
        return self.res
    
    def helper(self, root):
        if not root:
            return -1
        left = self.removeLeaves(root.left)
        right = self.removeLeaves(root.right)
        height = 1 + max(left, right)

        if len(self.res) < height + 1:
            self.res.append([])
        self.res[height].append(root.val)
        return height
class Solution:
    def findLeaves(self, root):
        if not root:
            return -1
        left = self.findLeaves(root.left)
        right = self.findLeaves(root.right)

        height = 1 + max(left, right)
        if len(self.res) < height+1:
            self.res.append([])
        self.res[height].append(root.val)
        return height
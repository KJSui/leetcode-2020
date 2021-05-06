class Solution:
    def longestUnivaluePath(self, root):
        self.res = 0
        self.helper(root)
        return self.res 

    def helper(self, root):
        if not root:
            return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        lr = rr = 0
        if root.left and root.left.val == root.val:
            lr = l + 1
        if root.right and root.right.val == root.val:
            rr = r + 1

        self.res = max(self.res, lr+rr)
        return max(lr, rr)
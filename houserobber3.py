class Solution:
    def rob(self, root):
        n = self.helper(root)
        return max(n[0], n[1])

    def helper(self, root):
        if not root:
            return [0, 0]
        if not root.left and not root.right:
            return [root.val, 0]
        l = self.helper(root.left)
        r = self.helper(root.right)
        withroot = max(l[1], r[1]) + root.val
        withoutroot = max(l[0], l[1]) + max(r[0], r[1])
        return [withroot, withoutroot]
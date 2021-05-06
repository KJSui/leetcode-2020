class Solution:
    def maxAncestorDiff(self, root):
        if not root:
            return 0
        res = self.helper(root)
        return res[2]

    def helper(self, root):
        if root and not root.left and not root.right:
            return (root.val, root.val, 0)
        minv = root.val
        maxv = root.val
        maxdiff = 0

        if root.left:
            left_min, left_max, left_diff = self.helper(root.left)
            minv = min(minv, left_min)
            maxv = max(maxv, left_max)
            maxdiff = max(maxdiff, self.differ(root.val, left_min, left_max, left_diff))
        if root.right:
            right_min, right_max, right_diff = self.helper(root.right)
            minv = min(minv, right_min)
            maxv = max(maxv, right_max)
            maxdiff = max(maxdiff, self.differ(root.val, right_min, right_max, right_diff))

        return (minv, maxv, maxdiff)

    def differ(self, nodeval, minv, maxv, resv):
        diffmin = abs(nodeval-minv)
        diffmax = abs(nodeval-maxv)
        return max(resv, diffmin, diffmax)

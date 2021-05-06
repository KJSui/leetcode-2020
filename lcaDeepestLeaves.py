class Solution:
    def lcaDeepestLeaves(self, root):

    def dsf(self, root):
        if not root:
            return [None, 0]
        left = self.dsf(root.left)
        right = self.dsf(root.right)
        maxdepth = max(left[1], right[1])
        if left[1] == right[1]:
            return [root, maxdepth+1]
        if left[1] > right[1]:
            return [left[0], maxdepth+1]
        if left[1] < right[1]:
            return [right[0], maxdepth+1]
            

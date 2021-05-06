class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = self.dfs(root)
        return res[2]
    def dfs(self, node):
        if not node.left and not node.right:  #leaf
            return (node.val, node.val, 0)
        min_val = node.val
        max_val = node.val
        max_diff = 0
        if node.left:
            (left_min, left_max, left_res) = self.dfs(node.left)
            max_diff = max(max_diff, self.diff_helper(node.val, left_min, left_max, left_res))
            min_val = min(min_val, left_min)
            max_val = max(max_val, left_max)
        if node.right:
            (right_min, right_max, right_res) = self.dfs(node.right)
            max_diff = max(max_diff, self.diff_helper(node.val, right_min, right_max, right_res))
            min_val = min(min_val, right_min)
            max_val = max(max_val, right_max)
        return (min_val, max_val, max_diff)
    
    def diff_helper(self, cur_val, min_val, max_val, max_diff):
        diff_from_min = abs(cur_val - min_val)
        diff_from_max = abs(cur_val - max_val)
        return max(max_diff, max(diff_from_min, diff_from_max))
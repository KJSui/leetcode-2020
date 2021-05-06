class Solution:
    #binaryTree
    def maxPathLen(self, node, prev_val, prev_len):
        if not node:
            return prev_len

        if node.val == prev_val + 1:
            return max(self.maxPathLen(node.left, node.val, prev_len+1), self.maxPathLen(node.right, node.val, prev_len+1))

        new_path_len = max(self.maxPathLen(node.left, node.val, 1), self.maxPathLen(node.right, node.val, 1))

        return max(new_path_len, prev_len)

    #binarySearchTree
    def maxPathLenBST(self, node, prev_val, prev_len, left_tree):
        if not node:
            return prev_len
        if left_tree:
            if node.val == prev_val - 1:
                left = self.maxPathLenBST(node.left, node.val, prev_len+1, True)
                right = self.maxPathLenBST(node.right, node.val, prev_len+1, False)

        else:
            if node.val == prev_val + 1:
                return max(self.maxPathLenBST(node.left, node.val, prev_len+1, True),
                            self.maxPathLenBST(node.right, node.val, prev_len+1, False))

        new_path = return max(self.maxPathLenBST(node.left, node.val, 1, True),
                            self.maxPathLenBST(node.right, node.val, 1, False))
        return max(new_path, prev_len)

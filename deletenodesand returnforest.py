class Solution:
    def delNode(self, root, to_delete):
        st = set(to_delete)
        res = []
        if root.val not in st:
            res.append(root.val)
        def helper(self, root, parent, direct):
            if not root:
                return None
            if root.val in st:
                if parent and direct == 'L':
                    parent.left = None
                if parent and direct == 'R':
                    parent.right = None
                if root.left and root.left.val not in st:
                    res.append(root.left.val)
                if root.right and root.right.val not in st:
                    res.append(root.right.val)
            helper(root.left, root, 'L')
            helper(root.right, root, 'R')

        helper(root, None, 'L')
        return res
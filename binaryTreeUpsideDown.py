class Solution:
    def upsideDownBinaryTree(self, root):
        p = root 
        parent = None 
        right = None 
        self.helper(p, parent, right)
        return parent


    def helper(self, root, parent, right):
        if not root:
            return 
        left = root.left 
        root.left = right 
        right = root.right 
        root.right = parent 
        self.helper(left, root, right) 
        return 

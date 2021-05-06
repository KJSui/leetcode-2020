class Solution:
    def flattenBianryTree(self, root):
        self.helper(root)
        return None 

    def helper(self, root):
        if root:
            self.helper(root.left)
            self.helper(root.right)

        if root.left:
            self.left, self.right = root.left, root.right 
            root.right, root.left = self.left, None 
            while self.left.right:
                self.left = self.left.right 

            self.left.right = self.right 

        
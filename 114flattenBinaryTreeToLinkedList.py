class Solution:
    def flatten(self, root):
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            self.left, self.right = root.left, root.right
            root.right, root.left = self.left, None
            while self.left.right:
                self.left = self.left.right
            self.left.right = self.right
            

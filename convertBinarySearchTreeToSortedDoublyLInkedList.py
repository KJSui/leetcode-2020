class Solution:
    def treeToDoublyList(self, root):
        self.first, self.last = None, None
        if not root:
            return None
        self.dfs(root)
        self.first.left = self.last
        self.last.right = self.first
        return self.first

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        if self.last:
            self.last.right = root
            root.left = self.last
        else:
            self.first = root

        self.last = root
        self.dfs(root.right)
        return
        

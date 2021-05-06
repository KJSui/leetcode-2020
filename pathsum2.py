class Solution:
    def pathSum2(self, root, sum):
        self.res = []
        self.array = []

    def helper(self, root, sum):
        if not root:
            return 
        if not root.left and not root.right:
            if sum - root.val == 0:
                self.array.append(root.val)
                self.res.append(self.array[:])
            else:
                self.array.append(root.val)

        else:
            self.array.append(root.val)
        self.helper(root.left, sum-root.val)
        self.helper(root.right, sum-root.right)
        if len(self.array) > 0:
            self.array.pop()
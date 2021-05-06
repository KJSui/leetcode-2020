class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False 
        if sum - root.val and not root.left and not root.right:
            return True 
        sum -= root.val
        left = self.hasPathSum(root.left, sum)
        right = self.hasPathSum(root.right, sum)
        return left or right 



    
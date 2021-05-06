 class TreeNode(object):
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root or (not root.left and not root.right):
            return False

        self.res = []
        self.helper(root, root.left, 1, x, y)
        self.helper(root, root.right, 1, x, y)
        if len(self.res) == 2:
            d1 = self.res[0][1]
            p1 = self.res[0][0]
            d2 = self.res[1][1]
            p2 = sefl.res[1][0]
            if d1 > 0 and d1 == d2 and p1 and p2 and p1.val != p2.val:
                return True
        return False
    
    def helper(self, parent, root, depth, x, y):
        if not root:
            self.res.append((parent, 0))
            return
        if root.val == x or root.val == y:
            self.res.append((parent, depth))
            return
        
        self.helper(root, root.left, depth+1, x, y)
        self.helper(root, root.right, depth+1, x, y)
        
        return
            
obj = Solution()

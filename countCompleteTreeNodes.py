class Solution:
    def countNodes(self, root):
        lh = lr = 0
        lnode = rnode = root
        while lnode:
            lh += 1
            lnode = lnode.left

        while rnode:
            lr += 1
            rnode = rnode.right

        if lh == rh:
            return pow(2, lh)-1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right)+1
            
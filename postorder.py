class Solution:
    def postOrder(self, root):
        if not root:
            return None
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.val)

    def postOrderTraverse(self, root):
        stack = []
        res = []
        while True:
            while root:
                stack.append(root)
                root = root.left 

            currRight = None 
            while stack:
                root = stack.pop()
                if root.right == currRight:
                    res.append(root.val)
                    currRight = root 
                else:
                    stack.append(root)
                    root = root.right 

                    break 

            if len(stack) == 0:
                break

        return res  
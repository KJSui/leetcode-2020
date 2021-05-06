class Solution:
    def binaryTreePostOrder(self, node):
        stack = []
        res = []
        stack.append(node)
        while True:
            while node:
                stack.append(node)
                node = node.left

            q = None
            while len(stack):
                p = stack.pop()
                if p.right == q:
                    res.append(p.val)
                    q = p
                else:
                    stack.append(p)
                    p = p.right
                    break
            if len(stack) == 0:
                break 

        return res
                    
        2
    1       3
4       5
    6


2, 3
q = 1, p = 2

res = 4, 6, 5,1, 
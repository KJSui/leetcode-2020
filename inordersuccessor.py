class Solution:
    def inorderSuccessor(self, root, p):
        if p.right:
            return self.findSuccessor(p.right)
        
        stack = []
        inorder = float('inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left 
            root = stack.pop()
            if inorder == p.val:
                return root 
            inorder = root.val 
            root = root.right 
        return None 

    def findSuccessor(self, node):
        while node.left:
            node = node.left 
        return node 


            

class Solution:
    def buildtree(self, preorder, inorder):
        if not inorder:
            return 
        inorderIndex = inorder.index(preorder.pop(0))    
        root = TreeNode(inorder[inorderIndex])
        root.left = self.buildtree(preorder, inorder[:inorderIndex])
        root.right = self.buildtree(preorder, inorder[inorderIndex+1:])
        return root 


    
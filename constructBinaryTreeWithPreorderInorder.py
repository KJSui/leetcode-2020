class Solution:
    def constructTree(self, inorder, preorder):
        if inorder:
            idx = inorder.index(preorder.pop(0))
            root = Node(inorder[idx])
            root.left = self.constructTree(inorder[:idx], preorder)
            root.right = self.constructTree(inorder[idx+1:], preorder)
            return root

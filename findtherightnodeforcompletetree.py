class Solution:
    def findTheRightestNode(self, root):
        if not root or (not root.left and not root.right):
            return root

        depth = 0
        currNode = root
        while currNode:
            depth += 1
            currNode = currNode.left

        tmpDepth = 0
        level = 0
        while root:
            level += 1
            if level == depth:
                break
            currNode = root
            if currNode.right:
                tmpDepth = level + 1
                parent = currNode
                currNode = currNode.right
                while currNode.left:
                    tmpDepth += 1
                    prent = currNode
                    currNode = currNode.left
                if temDepth < depth:
                    root = root.left
                elif not parent.right or parent.right == currNode:
                     return curNode
                else:
                    root = root.right 
            else:
                root = root.left

        return root

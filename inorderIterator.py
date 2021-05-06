class Solution:
    def inorderIterator(self, root):
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            print(curr.val)
            
            curr = curr.right 
        

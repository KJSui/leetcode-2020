class Solution:
    def __init__(self, root):
        self.stack = []
        curr = root
        while curr:
            self.stack.append(curr)


    def binarySearchTreeIteratorNext(self):
        node = self.stack.pop()
        curr = node
        if curr.right:
            curr = curr.right
            while curr:
                self.stack.append(curr)
                curr = curr.left
        return node.val

    def hasNext(self):
        if len(self.stack) > 0:
            return True
        return False


class solution:
    def popuNextRight(self, root):
        if not root:
            return 
        dummy = Node(-1)
        prev = dummy 
        curr = root 
        while curr:
            if curr.left:
                prev.next = curr.left 
                prev =   prev.next 
            if curr.right:
                prev.next = curr.right 
                prev = prev.next 

            curr = curr.next 

        self.popuNextRight(dummy.next)

    def nextRightRecursive(self, root):
        while root:
            begin = next = None
            while root:
                if not next:
                    if root.left:
                        next = root.left
                    else:
                        next = root.right 
                
                if root.left:
                    if begin:
                        begin.next = root.left
                    begin = root.left 
            
                if root.right:
                    if begin:
                        begin.next = root.right 
                    begin = root.right
                root = root.next 
            root = next
                
                    

        
class Solution:
    def merge(self, node1, node2):
        s1, s2 = None, None 
        c1, c2 = node1, node2 
        if c1 is None:
            self.inorder(c2)
            return 
        if c2 is None:
            self.inorder(c1)
            return 
        while s1 or s2 or c1 or c2:
            if c1 or c2:
                if c1:
                    s1.append(c1)
                    c1 = c1.left 

                if c2:
                    s2.append(c2)
                    c2 = c2.left 

            else:
                if s1 is None:
                    while s2:
                        c2 = s2.pop()
                        c2.left = None 
                        self.inorder(c2)

                    return 

                if s2 is None:
                    while s1:
                        c1 = s1.pop()
                        c1.left = None 
                        self.inorder(c1)

                c1 = s1.pop()
                c2 = s2.pop()

                if c1.val < c2.val:
                    res.append(c1.val)
                    c1 = c1.right 
                    s2.append(c2)
                    c2 = None 
                else:
                    res.append(c2.val)
                    c2 = c2.right 
                    s1.append(s1)
                    c1 = None 

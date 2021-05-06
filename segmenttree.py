class segmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.sum = 0
class NumArray:
    def __init__(self, nums):
        
    def buildSegmentTree(self, nums, start, end):
        if start > end:
            return None
        else:
            res = segmentTreeNode(start, end)
            if start == end:
                res.sum = nums[start]
            else:
                mid = start + (end - start)/2
                res.left = self.buildSegmentTree(nums, start, mid)
                res.right = self.buildSegmentTree(nums, mid+1, end)
                res.sum = res.left.sum + res.right.sum
        return res

    def updateTree(self, i, val):
        tmplist = []
        p = self.root
        while p.left != p.right:
            tmplist.append(p)
            mid = (p.start + p.right)/2
            if i <= mid:
                p = p.left
            else:
                p = p.right

        p.sum = val
        while sk:
            k = tmplist.pop()
            k.sum = k.left.sum + k.right.sum
    
    def sumrange(self, i, j):
        return self.sumrangehelper(self.root, i, j)

    def sumrangehelper(self, root, start, end):
        if root.start == start and root.end == end:
            return root.sum
        else:
            mid = start + (end-start)/2
            if end <= mid:
                return self.sumrangehelper(root.left, start, end)
            elif start > mid:
                return self.sumrangehelper(root.right, start, end)
            else:
                return self.sumrangehelper(root.left, start, mid) + self.sumrangehelper(root.right, mid+1, end)
                


            
        
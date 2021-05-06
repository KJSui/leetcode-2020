class Solution:
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums 
        pivot = int(len(nums)/2)
        left = self.merge_sort(nums[:pivot])
        right = self.merge_sort(nums[pivot:])
        return self.merge(left, right)


    def merge(self, left, right):
        res = []
        l = len(left)
        r = len(right)
        while i < l and j < r:
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
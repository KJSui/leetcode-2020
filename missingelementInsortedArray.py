class Solution:
    def missingElement(self, nums, k):
        n = len(nums)
        if k > self.missing(nums, n-1):
            return nums[n-1] + k - missing(n-1)
        left, right = 0, n-1
        while left < right:
            pivot = left + (right-left)//2
            if self.missing(nums, pivot) < k:
                left = pivot + 1
            else:
                right = pivot

        return nums[left-1] + k - self.missing(left-1)

    def missing(self, nums, idx):
        return nums[idx]-nums[0]-idx

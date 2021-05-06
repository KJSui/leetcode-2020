class Solution:
    def splitArray(self, nums, m):
        left = max(nums)
        right = sum(nums)
        if m == 1:
            return right

        while left <= right:
            mid = int((left + right)/2)
            if self.helper(mid, nums, m):
                right = mid - 1
            else:
                left = mid+1

        return left

    def helper(self, mid, nums, m):
        s = 0
        for i in range(0, len(nums)):
            if s + nums[i] > mid:
                m -= 1
                s = nums[i]
                if m < 1:
                    return False
            else:
                s += nums[i]

        return True
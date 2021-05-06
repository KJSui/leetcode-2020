class Solution:
    def maxSlidingWindow(self, nums, k):
        dp = []
        res = []
        for i in range(len(nums)):
            if len(dp) > 0 and i-k == dp[0]:
                dp.pop(0)
            while len(dp) > 0 and nums[dp[-1]] < nums[i]:
                dp.pop()
            dp.append(i)
            if i >= k-1:
                res.append(nums[dp[0]])

        return res
            

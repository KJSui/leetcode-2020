class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        dp = []
        for i in range(len(nums)):
            if len(dp) > 0 and dp[0] == i - k:
                dp.pop(0)

            while len(dp) > 0 and nums[dp[-1]] < nums[i]:
                dp.pop()

            dp.append(i)
            if i >= k-1:
                res.append(nums[dp[0]])

        return res
class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)
        f = [[0]*n for _ in range(n)]

        for left in range(n-2, -1, -1):
            for right in range(left+2, n):
                for i in range(left+1, right):
                    f[left][right] = max(nums[left]*nums[i[*nums[right] + f[left][i] + f[i][right])

        return nums[0][n-1]


#recurse method, memorizaiton

class Solution:
    def helper(self, memo, nums, left, right):
        if left + 1 == right:
            return 0

        if memo[left][right] > 0:
            return memo[left][right]

        ans = 0
        for i in range(left+1, right):
            ans = max(ans, nums[left]*nums[i]*nums[right]+self.helper(memo, nums, left, i)+self.helper(memo, nums, i, right))
        memo[left][right] = ans

        return ans
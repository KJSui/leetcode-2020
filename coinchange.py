class Solution:
    def coinChange(self, coins, amount):
        mx = amount + 1
        dp = [mx] * mx
        dp[0]  =0
        for i in range(amount+1):
            for j in coins:
                dp[i] = min(dp[i], dp[i-j]+1)

        return -1 if dp[amount] > amount else dp[amount]
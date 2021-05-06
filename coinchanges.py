class Solution:
    def coinchanges(self, coins, amount):
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for j in coins:
                if j <= i:
                    dp[i] = min(dp[i], dp[i-j]+1)
                else:
                    break
        return -1 if dp[amount] > amount else dp[amount]
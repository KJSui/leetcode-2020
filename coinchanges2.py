class Solution:
    def change(self, amount, coins):
        dp = [[0 for i in range(len(coins)+1)] for j in range(amount+1)]
        for i in range(len(coins)+1):
            dp[0][i] = 1

        for i in range(amount+1):
            for j in range(1, len(coins)+1):
                dp[i][j] = dp[i][j-1]
                if i >= coins[j-1]:
                    dp[i][j] += dp[i-coins[j-1]][j]

        return dp[amount][len(coins)]
        
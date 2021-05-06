class Solution:
    def coinchange(self, coins, amount):
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        res = []
        for i in range(amount+1):
            for j in coins:
                if i >= j:
                    dp[i] = min(dp[i-j]+1, dp[i])

        minamount = dp[amount]
        coinset = set(coins)
        for i in range(len(coins)-1, -1, -1):
            if amount >= coins[i]:
                while amount >= coins[i] and minamount:
                    minamount -= 1
                    amount -= coins[i]
                    res.append(coins[i])
                if minamount == 0 and amount == 0:
                    break
                elif minamount > 0 and amount <= 0:
                    res.pop()
                    minamount += 1
                    amount += coins[i]
                
                elif minamount == 0 and amount > 0:
                    res.pop()
                    minamount += 1
                    amount += coins[i]
        

        print("coinchange:res", res)
        return -1 if dp[amount] > amount else dp[amount]

obj = Solution()
coins = [1, 2, 5]
amount = 11
print(obj.coinchange(coins, amount))

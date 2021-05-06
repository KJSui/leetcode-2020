class Solution:
    def personWeight(self, load, weight, isVip):
        dp = [[0 for i in range(load+1)] for j in range(len(weight)+1)]

        for i in range(1, len(weight)+1):
            for j in range(1, load+1):
                if j < weight[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i-1]] + (2 if isVip[i-1] == 1 else 1))
                #print("i:", i, "j:", j, "dp[i-1][j]:", dp[i-1][j], "dp[i][j]:", dp[i][j])
            print("\n")
        return dp[len(weight)][load]

obj = Solution()
load = 120
weight = [40, 50, 60, 80]
isVip = [0, 0, 1, 1]
print(obj.personWeight(load, weight, isVip))

class Solution:
    def coins(self, n):
        dp = [False]*(n+1)
        flag = [False]*(n+1)

        return self.helper(i, dp, flag)

    def helper(i, dp, flag):
        if flag[i]:
            return dp[i]
        if i == 0:
            dp[i] = False 
        elif i == 1:
            dp[i] = True 
        elif i == 2:
            dp[i] = True 
        else:
            dp[i] = not self.helper(i-1, dp, flag) or not self.helper(i-2, dp, flag)

        flag[i] = True 
        return dp[i]
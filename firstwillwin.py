class Solution:
    def firstWillWin(self, n):
        dp = [False] * (n+1) 
        flag = [False] * (n+1)
        
    def memorySearch(self, i, dp, flag):
        if flag[i] == True:
            return dp[i]

        if i == 0:
            dp[0] = False 
        elif i == 1:
            dp[1] = True 

        elif i == 2:
            dp[2] = True 
        
        else:
            dp[i] = not self.memorySearch(i-1, dp, flag) or not self.memorySearch(i-2, dp, flag)

        flag[i] = True 

        return dp[i]


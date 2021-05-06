class Solution:
    def canJump(self, pos, nums):
        if pos == len(nums) - 1:
            return True
        
        jumplen = min(nums[pos]+pos, len(nums)-1)
        for j in range(pos+1, jumplen+1):
            if self.canJump(j, nums):
                return True
        
        return False

from enum import Enum
#bottonn-top DP
class Index(Enum):
    GOOD = 1 
    BAD = 2
    UNKOWN = 3
}
class Solution:
    def canJump(self, pos, nums):
        dp = [Index.UNKOWN]*len(nums)
        dp[-1] = Index.GOOD
        for j in range(len(nums)-2), -1, -1):
            numjump = min(nums[j]+j, len(nums)-1)
            for i in range(j+1, len(nums)):
                if dp[i] == GOOD:
                    dp[j] = GOOD
                    break
        return dp[0] == index(GOOD)
                

    
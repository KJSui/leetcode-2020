class Solution:
    #backtracking method
    def canJump(self, start, nums):
        if start == len(nums)-1:
            return True 
        
        furthestJump = min(nums[start]+start, len(nums)-1)

        for nextPosition in range(start+1, furthestJump+1):
            if self.canJump(nextPosition, nums):
                return True

        return False 




    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        reach = j = 0
        while j < len(nums) and j<= reach:
            reach = max(reach, j + nums[j])
            j += 1
        return reach >= len(nums)-1

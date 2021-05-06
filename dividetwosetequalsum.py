class Solution:
    def canPartition(self, nums):
        nums.sort()
        total = sum(nums)
        if total%2 == 1:
            return False
        sub = total/2
        if sub < nums[-1]:
            return False
        print("nums: ", nums, "sub: ", sub, "total: ", total)
        for i in range(len(nums)-1, -1, -1):
            if self.dfs(nums[:i], sub-nums[i]):
                return True
        return False
    
    def dfs(self, nums, sub):
        if sub == 0:
            return True
        if sub < 0 or len(nums) == 0:
            return False
        
        mid = self.bst(nums, sub)
        print("dfs: mid: ", mid, "sub: ", sub, "nums: ", nums)
        if mid < 0:
            return False
        if nums[mid] == sub:
            return True
        sub -= nums[mid]
        return self.dfs(nums[:mid], sub)  
        
    def bst(self, nums, target):
        l, r = 0, len(nums)-1
        while l+1 < r:
            mid = l + int((r-l)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid
            else:
                r = mid
                
        if nums[l] > target:
            return l-1
        elif nums[r] <= target:
            return r
        else:
            return l

obj = Solution()
nums = [23, 13, 11, 7, 6, 5, 5]
print(obj.canPartition(nums))
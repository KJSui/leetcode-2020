class Solution:
    def twoSum(self, target, nums):
        mp = {}
        for i in range(len(nums)):
            if target - nums[i] in mp.keys():
                return [mp[target-nums[i]], i]
            else:
                mp[nums[i]] = i
        return [-1, -1]

obj = Solution()
target = 6
nums = [2, 3, 4, 5]
print(obj.twoSum(target, nums))

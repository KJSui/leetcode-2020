class Solution:
    def backpack(self, nums, target):
        nums = sorted(nums)
        self.res = []
        self.dfs(nums, target, 0, [])
        return self.res


    def dfs(self, nums, target, idx, lt):
        if target == 0:
            self.res.append(lt[:])
            return
        if idx == len(nums) or target < 0:
            return

        #key = str(idx) + "-" + str(target)
        for j in range(idx, len(nums)):
            self.dfs(nums, target-nums[j], j, lt + [nums[j]])

        return


obj = Solution()
nums = [1, 2, 3]
target = 6
print(obj.backpack(nums, target))

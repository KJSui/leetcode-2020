class Solution:
    def makesquare(self, nums):
        targetsum = sum(nums)/4
        if targetsum * 4 != sum(nums):
            return False

        if len(num) == 0 or int(targetsum) != targetsum:
            return False

        visited = [False] * len(nums)

        def dfs(start, nums, visited, k, currSum, targetsum):
            if k == 1:
                return True
            if currSum == targetsum:
                return dfs(0, nums, k-1, 0, targetsum)

            for i in range(start, len(nums)):
                if visited[start] == False:
                    visited[start] = True
                    if(dfs(i+1, nums, visited, currSum+nums[i], targetsum)):
                        return True
                    visited[i] = False

            return False s

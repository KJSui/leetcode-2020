class Solution:
    def depthSum(self, nestedList):
        return self.dfs(nestedList, 1, 1)

    def dfs(self, nestedList, prevlevel, level):
        res = 0
        for i in nestedList:
            if type(i) is not list:
                res += prevlevel * level * i
            else:
                res += self.dfs(i, level, level+1)
        return res
obj = Solution()
nestedList = [1, [4, [6]]]
print(obj.depthSum(nestedList))

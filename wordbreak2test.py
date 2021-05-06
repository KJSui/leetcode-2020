import collections
class Solution:
    def wordBreak(self, s, wordDict):
        self.mp = collections.defaultdict(list)
        return self.dfs(s, 0, wordDict)


    def dfs(self, s, start, wordDict):
        if start in self.mp:
            return self.mp[start]
        if start == len(s):
            return [""]
        res = []
        for end in range(start+1, len(s)+1):
            if s[start:end] in wordDict:
                lt = self.dfs(s, end, wordDict)
                for i in lt:
                    m = ""
                    if i != m:
                        m = " "
                    res.append(s[start:end] + m + i)
        self.mp[start] = res[:]
        return res
obj = Solution()
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(obj.wordBreak(s, wordDict))

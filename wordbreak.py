class Solution:
    def wordBreak(self, s, wordDict):
        wordDictSet = set(wordDict)
        cache = [0]*len(s)
        res = self.dfs(s, wordDictSet, 0, cache)
        if res == 1:
            return True
        return False
    def dfs(self, s, wordDictSet, start, cache):
        print("start: ", start, "word: ", s[start], "cache: ", cache)
        if start == len(s):
            return 1 
        if cache[start] != 0:
            return cache[start]
        for i in range(start+1, len(s)+1):
            if (s[start:i] in wordDictSet) and (self.dfs(s, wordDictSet, i, cache) == 1):
                print("s[start:i]: ", s[start:i], "start: ", start, "i: ", i)
                cache[start] = 1
                return 1
        cache[start] = -1
        return cache[start]

obj = Solution()
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(obj.wordBreak(s, wordDict))
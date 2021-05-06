class Solution:
    def constructTarget(self, dict, word):
        self.res = []
        self.map = {}
        self.dfs(dict, word, 0, 0, [])
        return self.res

    def dfs(self, dt, word, widx, idx, lt):
        if widx >= len(word):
            self.res.append(lt[:])
            return lt
        if :
            return
        for j in range(0, len(dt)):
            if dt[j] == word[widx:widx+len(dt[j])]:
                res = self.dfs(dt, word, widx+len(dt[j]), j, lt + [dt[j]])
            self.map[widx].append(lt[j:])

        return

obj = Solution()
#dict = ['abc', 'defg', 'de', 'fg']
#word = 'abcdefg'
dict = ['a', 'aa']
word = 'aaa'
print(obj.constructTarget(dict, word))



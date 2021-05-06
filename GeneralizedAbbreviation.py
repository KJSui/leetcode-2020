class Solution:
    def generateAbbreviations(self, word):
        ans = []
        ret = []
        self.helper(ret, word, 0, "", 0)
        return ret
    def helper(self, ret, word, pos, cur, count):
        print("cur: ", cur, "count: ", count, "pos: ", pos, "ret:", ret)
        if pos == len(word):
            if count > 0:
                cur += str(count)
            ret.append(cur)
        else:
            self.helper(ret, word, pos+1, cur, count+1)
            self.helper(ret, word, pos+1, cur + str((count if count > 0 else "")) + word[pos], 0)
            
            

object = Solution()
word = "rs"
print(object.generateAbbreviations(word))
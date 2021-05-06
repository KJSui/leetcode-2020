class Solution:
    def removeConsequentLetter(self, s):
        if len(s) <= 1:
            return s 
        prev = 0
        curr = 1
        while curr < len(s):
            if s[curr] == s[prev]:
                s = s[:prev] + s[curr+1:]
                prev -= 1
                curr -= 1
                if prev < 0:
                    prev = 0
                    curr = 1
            else:
                prev += 1
                curr += 1

        return s

obj = Solution()
s = "abbcabb"
print(obj.removeConsequentLetter(s))
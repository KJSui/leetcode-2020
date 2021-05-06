class Solution:
    def deepestString(self, s):
        res = ""
        level = 0
        start = 0
        maxlevel = 0
        while start < len(s):
            if s[start] == '(':
                level += 1
                if maxlevel <= level:
                    maxlevel = level
                    res = ""
            elif s[start] == ')':
                level -= 1
            else:
                if level == maxlevel:
                    res += s[start]
            start += 1

        return res

obj = Solution()
s = "ab(c(d))e"
print(obj.deepestString(s))

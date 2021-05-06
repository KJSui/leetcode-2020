class Solution:
    def findAnagram(self, s, p):
        p = "".join(sorted(p))
        myset = set(p)
        curr= ""
        prev = ""
        start = 0
        res = []
        while start < len(s):
            if s[start] not in myset:
                curr = ""
                prev = ""
                start += 1
                continue 

            if len(curr) < len(p):
                curr += s[start]
                start += 1
                continue 

            if s[start] == prev:
                prev = curr[0]
                res.append(start-len(p)+1)
                curr = curr[1:]
                start += 1
                continue 

            if "".join(sorted(curr)) == p:
                res.append(start-len(p)+1)
                prev = curr[0]
                start += 1
                curr = curr[1:]
                continue 

            else:
                prev = ""
                curr = curr[1:]
                start += 1
        return res 
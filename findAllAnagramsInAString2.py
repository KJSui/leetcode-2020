class Solution:
    def findAllAnagram(self, s, p):
        p = "".join(sorted(p))
        p_set = set(p)
        prev = ""
        window = ""
        res = []
        for c in range(len(s)):
            if c not in p_set:
                window = ""
                prev = ""
                continue

            window += s[c]
            if len(window) < len(p):
                continue

            if prev == c:
                res.append(c - len(window)+1)
                prev = window[0]
                window = window[1:]
                continue

            if "".join(sorted(window)) == p:
                res.append(i-len(window)+1)
                prev = window[0]
            else:
                prev = ""

            window = window[1:]

        return res
                
            

class Solution:
    def findAnagrams(self, s, p):
        kset = set(p)
        klen = len(p)
        slidingwin = []
        res = []
        for i in s:
            if i not in kset:
                continue 
            slidingwin.append(i)
            if len(slidingwin) == klen:
                if i == prev:
                    res.append(i-klen+1)
                    prev = slidingwin[0]
                    slidingwin = slidingwin[1:]

                else:
                    if "".join(sorted(slidingwin)) == p:
                        res.append(i-klen+1)
                        prev = slidingwin[0]
                        slidingwin = slidingwin[1:]
                    else:
                        prev = ""
                        slidingwin = slidingwin[1:]
        return res

obj = Solution()
s = "123"
p = "321"
print(obj.findAnagrams(s, p))
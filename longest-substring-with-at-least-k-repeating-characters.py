class Solution:
    def longestSubstring(self, s, k):
        start = 0
        line = 0
        mp = {}
        res = 0
        st =set()
        while start < len(s):
            if s[start] not in mp:
                mp[s[start]] = 1
            else:
                mp[s[start]] += 1
            if mp[s[start]] >= k:
                st.add(s[start])
            line = len(st)
            if line == len(mp):
                res = max(res, start+1)
            print("mp:", mp, "st:", st, "start:", start, "res:", res)
            start += 1
        start = 0
        while len(s) - start > res:
            if s[start] not in st:
                if s[start] in mp:
                    mp[s[start]] -= 1
                    if mp[s[start]] == 0:
                        del mp[s[start]]
                        if len(mp) == len(st):
                            res = max(res, len(s) - start -1)
            else:
                
                mp[s[start]] -= 1
                if mp[s[start]] < k:
                    st.remove(s[start])
            start += 1
        return res

obj = Solution()
s = "bbaaacbd"
k = 3
print(obj.longestSubstring(s, k))
                    
            
            

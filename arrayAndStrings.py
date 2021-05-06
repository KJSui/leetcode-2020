class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k >= len(s):
            return len(s)
        if k <= 0:
            return 0
        mp = {}
        i = 0 
        l = 0
        start = 0
        while i < len(s):
            if s[i] not in mp:
                mp[s[i]] = 1
            else:
                mp[s[i]] += 1
            print("21: before while: i: ", i, "mp: ", mp, "start: ", start)
            while len(mp) > k:
                if s[start] in mp.keys():
                    mp[s[start]] -= 1
                    if mp[s[start]] == 0:
                        del mp[s[start]]
                start += 1
            print("28: after while, i: ", i, "mp: ", mp, "start: ", start)
            i += 1
            l = max(l, i - start)
            print("31: l value: ", l, "i+1: ", i, " start: ", start)
        return l
        
s = "abaccc"
k = 2
obj = Solution()
print(obj.lengthOfLongestSubstringKDistinct(s, k))
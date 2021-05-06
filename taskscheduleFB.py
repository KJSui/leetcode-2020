class Solution:
    def taskscheduleFBwithoutchangingorder(self, s, k):
        mp = {}
        window = ""
        start = 0
        end = 0
        for i in range(len(s)):
            if end - start == k:
                start += 1
            if s[i] in mp.keys():
                prevIndex = mp[s[i]]
                substring = window[start:prevIndex+1]
                start += len(substring)
                for j in substring:
                    if j in mp.keys():
                        del mp[j]
                window += " " * (k-(end-prevIndex))
            window += s[i]
            end = len(window)-1
            mp[s[i]] = end
        return window
obj = Solution()
s = "BCBCAAAB"
k = 2
print(obj.taskscheduleFBwithoutchangingorder(s, k))

            

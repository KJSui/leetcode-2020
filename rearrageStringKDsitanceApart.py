import heapq
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k < 2:
            return s
        mp = {}
        for i in s:
            mp[i] = mp.get(i, 0)+1
        
        if len(mp) == 1 and mp[s[0]] > 1:
            return ""
        
        if len(mp) > 1 and len(mp) < k:
            return ""
        
        queue = []
        for i in mp.keys():
            v = (-mp[i], i)
            heapq.heappush(queue, v)
        
        flagcount = 0
        tmpq = []
        ans = ""
        while len(queue) > 0:
            count, c = heapq.heappop(queue)
            ans += c
            flagcount += 1
            print("ans: ", ans, "c: ", c, "count: ")
            if count == -1:
                del mp[c]
            if count < -1:
                tmpq.append((count+1, c))
            print("tmpq: ", tmpq, "queue: ", queue)
            if flagcount >= k:
                while len(tmpq):
                    cand = tmpq.pop(0)
                    if cand[0]:
                        heapq.heappush(queue, cand)
                flagcount = 0
            if len(queue) == 0:
                while len(tmpq):
                    v = tmpq.pop(0)
                    print("len(queue) == 0 and tmpq: ", tmpq, "v[0]: ", v[0], "v[1]:", v[1])
                    if len(tmpq) == 0 and (v[0] < -1 or v[1] == ans[-1]):
                        return ""
                    
                    heapq.heappush(queue, v)
            
        if len(ans) == len(s):
            return ans
        return ""
                    

obj = Solution()
s = "aaabc"
k = 3
print(obj.rearrangeString(s, k))

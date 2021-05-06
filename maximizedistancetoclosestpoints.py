class Solution:
    def maxDistToClosest(self, seats):
        queue = []
        mp = {}
        start = 0
        end = len(seats)-1
        maxvalue = 0
        
        for i in range(len(seats)):
            if seats[i] == 1:
                queue.append(i)
                mp[i] = 0
                
        while queue:
            print("queue:", queue)
            k = queue.pop(0)
            nv = mp[k] + 1
            if k > start:
                if (k-1 not in mp.keys()) or ((k-1 in mp.keys()) and (mp[k-1] != 0) and (mp[k-1] > nv)):
                    mp[k-1] = nv
                    queue.append(k-1)
            if k < end:
                if (k+1 not in mp.keys()) or ((k+1 in mp.keys()) and (mp[k+1] != 0) and (mp[k+1] > nv)):
                    mp[k+1] = nv
                    queue.append(k+1)
        
        for i in mp.values():
            maxvalue = max(maxvalue, i)
        return maxvalue
                            
                        
obj = Solution()
seats = [1,0,0,0,1,0,1]
print(obj.maxDistToClosest(seats))
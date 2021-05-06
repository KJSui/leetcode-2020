
class Solution:
    def findTwoSubarray(self, array, K):
        self.mp = collections.defaultdict(list)
        self.findAll(array, K)
        minv = min(self.mp.keys())
        maxv = max(self.mp.keys())
        start = minv
        nt = start + 1
        res = []
        for k in self.mp.keys(): 
            self.mp[k] = sorted(self.mp[k])

        while start <= maxv:
            vlist = self.mp[start]
            quote = 2 - len(res)
            first = 0
            while quote > 0:
                
        res = []
        

    def findAll(self, array, K):
        start = 0
        end = 0
        while start < len(array) and end < len(array):
            if sum(array[start:end+1]) < K:
                end += 1
            elif sum(array[start:end+1]) == K:
                self.mp[end-start+1].append([start, end])
                end += 1
            else:
                start += 1

obj = Solution()
array = [2, 4, 1, 2, 3, 4, 5, 1]
K = 6
print(obj.findTwoSubarray(array, K))
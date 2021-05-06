import heapq
class Solution:
    def sortFrameGoogle(self, array, K):
        queue = []
        res = []
        start = 0
        while start < len(array):
            if len(queue) < K:
                heapq.heappush(queue, array[start])
            else:
                res.append(heapq.heappop(queue))
                heapq.heappush(queue, array[start])
            start += 1
        
        while len(queue):
            res.append(heapq.heappop(queue))
        return res

obj = Solution()
array = [0,10, 33, 6, 28, 9, 50]
K = 4
print(obj.sortFrameGoogle(array, K))
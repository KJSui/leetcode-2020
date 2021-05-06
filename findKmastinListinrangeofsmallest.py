import heapq
class Solution:
    def smallestRange(self, nums):
        pq = []
        for l in range(len(nums)):
            pair = (nums[l][0], l, 0)
            heapq.heappush(pq, pair)
        

        index = 0
        res = pq[-1][0] - pq[0][0]
        rge = [pq[0][0], pq[-1][0]]
        while True:
            print("heap: ", pq)
            if res >  pq[-1][0] - pq[0][0]:
                rge = [pq[0][0], pq[-1][0]]
            elif res == pq[-1][0] - pq[0][0] and rge[1] > pq[0][0]:
                rge = [pq[0][0], pq[-1][0]]
            v = heapq.heappop(pq)
            index = v[2]+1
            if index < len(nums[v[1]]):
                pair = (nums[v[1]][index], v[1], index)
                heapq.heappush(pq, pair)
            else:
                break
        return rge
nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
obj = Solution()
print(obj.smallestRange(nums))
    
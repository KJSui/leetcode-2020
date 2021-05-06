import heapq from collections
class Solution:
    def slidingWindowMedian(self, nums, k):
        lo_maxheap = []
        hi_minheap = []

        invalid_hash = {}

        for i in range(k):
            heapq.heappush(lo_maxheap, -nums[i])

        for i in range(k//2):
            heapq.heappush(hi_minheap, -heapq.heappop(lo_maxheap))

        balance = 0
        start = k
        while True:
            median = -heapq.heappop(lo_maxheap) if k and 1 else (-heapq.heappop(lo_maxheap)+heapq.heappop(hi_minheap))/2.0
            outnum = nums[start-k]
            innum = nums[start]
            start += 1
            invalid_hash[outnum] = invalid_hash.get(outnum, 0)+1
            balance = -1 if outnum <= -lo_maxheap[0] else 1

            if len(lo_maxheap) > 0 and innum <= -lo_maxheap[0]:
                balance += 1
                heapq.heappush(lo_maxheap, innum)

            else:
                balance -= 1
                heapq.heappush(hi_minheap, innum)

            if balance < 0:
                heapq.heappush(lo_maxheap, heapq.heappop(hi_minheap))
                balance += 1 

            else:
                heapq.heappush(hi_minheap, heapq.heappop(lo_maxheap))
                balance -= 1

            while lo_maxheap[0] in invalid_hash and invalid_hash[lo_maxheap[0]]:
                v = heapq.heappop(lo_maxheap)
                invalid_hash[v] -= 1

            while hi_minheap[0] in invalid_hash and invalid_hash[hi_minheap[0]]:
                v = heapq.heappop(hi_minheap)
                invalid_hash[v] -= 1

        return median

                

                
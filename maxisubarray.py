import sys 
class Solution:
    def maxSubarray(self, array):
        res = -float('inf')
        f = 0
        for i in (array):
            f = max(f+i, i)
            res = max(res, f)

        return res 

obj = Solution()
array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(obj.maxSubarray(array))


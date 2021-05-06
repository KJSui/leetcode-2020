import collections
class Solution:
    def getGap(self, nums):
        nums = sorted(nums)
        st = set()
        maxgap = nums[-1] - nums[0]
        res = []
        gapmap = collections.defaultdict(list)
        for i in range(len(nums)-1):
            k = i+1

            gap = nums[k] - nums[i]
            while gap in gapmap and nums[k] in gapmap[gap]:
                k += 1
                if k == len(nums):
                    break
                gap = nums[k] - nums[i]
            
            while k < len(nums):
                gap = nums[k] - nums[i]
                if gap in gapmap:
                    gapmap[gap].append(nums[k])
                else:
                    gapmap[gap] = [nums[i], nums[k]]
                k += 1
            print("dict: ", gapmap)
        for i in range(1, maxgap+1):
            if i in gapmap:
                res.append(gapmap[i])
        return res
"""

class Solution:
    def getGap(self, nums):
        nums = sorted(nums)
        st = set()
        maxgap = nums[-1] - nums[0]
        res = []
        gapmap = collections.defaultdict(list)
        for i in range(len(nums)-1):
            k = i+1
            while k < len(nums):
                tmp = [nums[i]]
                j = k
                gap = nums[j] - nums[i]
                nt = i
                while j < len(nums):
                    if nums[j] - nums[nt] == gap:
                        tmp.append(nums[j])
                        nt = j  
                    j += 1

                res.append(tmp)
                k += 1
        return res  
"""
obj = Solution()
nums = [2, 4, 6, 8, 10]
print(obj.getGap(nums))
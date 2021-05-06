'''
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:     
        missarray = []
        if len(nums) == 0:
            if upper - lower > 0:
                missarray.append(str(lower)+"->"+str(upper))
            elif upper == lower and lower >= 0:
                missarray.append(str(lower))
            return missarray
        if lower == upper and lower < 0:
            return []        
        
        start = self.bs(nums, lower, 1)
        end = self.bs(nums, upper, 0)
        s = ""
        if start == -1 or lower < nums[start]:
            if start == -1:
                if nums[0] - lower > 2:
                    s = str(lower)+"->"+str(nums[0]-1)
                elif nums[0] - lower > 1:
                    s = str(lower)
            elif nums[start] - lower > 2:
                s = str(lower)+"->"+str(nums[start]-1)
            elif nums[start] - lower > 1:
                s = str(lower)       
            missarray.append(s)
            
        final = ""
        if end == len(nums):
            if upper - nums[-1] > 2:
                final = str(nums[-1]+1)+"->"+str(upper)
            elif upper - nums[-1] > 1:
                final = str(upper)
        elif upper - nums[end] > 2:
            final = str(nums[end]+1)+"->"+str(upper)
        elif upper - nums[end] > 1:
            final = str(upper)

        while start + 1< end:
            if nums[start+1] - nums[start] > 2:
                missarray.append(str(nums[start]+1)+"->" + str(nums[start+1]-1))
            elif nums[start+1] - nums[start] > 1:
                missarray.append(str(nums[start]+1))
            start += 1
        
        missarray.append(final)
        return missarray
        
    def bs(self, nums, k, left):
        if nums[0] > k:
            return -1
        if nums[-1] < k:
            return len(nums)
        
        start = 0
        end = len(nums)-1
        while start + 1 < end:
            mid = int((start + end)/2)
            if nums[mid] < k:
                start = mid
            elif nums[mid] == k:
                return mid
            else:
                end = mid
        if left:
            if nums[end] == k or nums[end] > k and nums[start]<k:
                return end
            return start
        else:
            if nums[start] == k or nums[end] > k and nums[start]<k:
                return start
            return end        

'''
"""
class Solution:
    def findMissingRanges(self, nums, lower, upper):
        i, res = 0, []
        nums = nums + [upper+1]
        while lower <= upper:
            if nums[i] > lower:
                if nums[i] - lower == 1:
                    res.append(str(lower))
                else:
                    res.append(str(lower) + '->' + str(nums[i]-1))
            lower, i = nums[i] + 1, i+1
        return res
"""

class Solution: 
    def bs(self, nums, k, left):
        print("nums: ", nums, "key: ", k)      
        start = 0
        end = len(nums)-1
        while start + 1 < end:
            mid = int((start + end)/2)
            if nums[mid] < k:
                start = mid
            elif nums[mid] == k:
                return nums[mid]
            else:
                end = mid
        if left:
            if nums[end] <= k:
                return nums[end]
            return nums[start]
        else:
            if nums[end] <= k or nums[end] > k and nums[start]<k:
                return nums[end]
            return nums[start]

obj = Solution()
nums = [0, 3, 4, 6]
print(obj.bs(nums, 1, 0))


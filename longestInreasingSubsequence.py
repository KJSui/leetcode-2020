class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = 0
        tails = [0]*len(nums)
        for x in nums:
            i, j = 0, size
            while i != j:
                m = int((i+j)/2)
                if tails[m] < x:
                    i = m+1
                else:
                    j = m
            tails[i] = x
            print("tails: ", tails, "i: ", i, "num: ", x)
            size = max(i+1, size)
        return size

obj = Solution()
nums = [10,9,2,4, 5,3,7,101,18]
print(obj.lengthOfLIS(nums))

class Solution:
    def lengthofLIS(self, nums):
        size = 0
        tails = [0]*len(nums)
        for x in nums:
            i, j = 0, size
            while i != j:
                m = int((i+j)/2)
                if tails[m] < x:
                    i = m+1
                else:
                    j = m
            tails[i] = x
            size = max(i+1, size)

        return size
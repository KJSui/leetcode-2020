class Solution:
    def permute(self, nums):
        def backtrack(first=0):
            if first == n:
                output.append(nums[:])
            else:
                for i in range(first, n):
                    nums[first], nums[i] = nums[i], nums[first]
                    print("nums: ", nums, "first: ", first, "i: ", i)
                    backtrack(first+1)
                    nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output 

obj = Solution()
nums = [1, 2, 3]
print(obj.permute(nums))
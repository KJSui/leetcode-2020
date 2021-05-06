class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1]*len(nums)
        for i in range(2 * len(nums)-1, -1, -1):
            if len(stack) and nums[stack[-1]] < nums[i]:
                stack.pop()
            if len(stack) == 0:
                res[i%len(nums)] = -1
            else:
                res[i%len(nums)] = nums[stack[-1]]
            stack.append(i%len(nums))
        return res

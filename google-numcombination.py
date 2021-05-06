class Solution:
    def numcombo(self, nums):
        self.res = []
        self.dic = {'1': ['a', 'b', 'c'], '2': ['d', 'e', 'f'], '3':['h', 'j', 'k']}
        self.helper(nums, 0, "")
        return self.res

    def helper(self, nums, index, s):
        if index == len(nums):
            self.res.append(s)
            return
        q = self.dic[nums[index]]
        for i in q:
            self.helper(nums, index+1, s+i)
        return

obj = Solution()
nums = "123"
print(obj.numcombo(nums))


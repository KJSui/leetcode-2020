from operator import truediv, mul, add, sub
class Solution:
    def judgePoint24(self, nums):
        length = len(nums)
        if not nums:
            return False
        if length == 1:
            return abs(nums[0]-24) < 1e-6
        for i in range(length):
            for j in range(length):
                if i != j:
                    B = [nums[k] for i in range(length) if i != j != k]
                    for op in (truediv, mul, add, sub):
                        if op in (mul, add) and j > i:
                            continue
                        if op is not truediv or A[j]:
                            B.append(op(nums[i], nums[j]))
                            if self.judgePoint24(B):
                                return True
                            B.pop()
        return False

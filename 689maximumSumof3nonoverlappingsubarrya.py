class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        res = []
        sm = 0
        for i in range(len(nums)):
            sm += nums[i]
            if i >= k:
                sm -= nums[i-k]
            if i >= k-1:
                res.append(sm)

        left = [0] * len(res)
        right = [0] * len(res)
        best = 0
        for i in range(len(res)):
            if w[i] > res[best]:
                best = i
            left[i] = best

        best = len(res)-1
        for i in range(len(w)-1, -1, -1):
            if w[i] > res[best]:
                best = i
            right[i] = best

        ans = None 
        for j in range(k, len(res)-k):
            if ans is None or res[left[j-k]] + res[j] + res[right[j+k]] > res[ans[0]] + res[ans[1]] + res[ans[2]]:
                ans = i, j, m
        return ans

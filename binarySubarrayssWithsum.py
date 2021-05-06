class Solution:
    def numSubarrayWithSum(self, A, S):
        array = [0]
        for i in A:
            array.append(array[-1]+i)
        mp = collections.Counter()
        res = 0
        for i in array:
            res += mp[i]
            mp[i+S] += 1

        return res

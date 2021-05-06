class Solution:
    def ksumtotarget(self, nums, k, target):
        for k in range(K+1):
            for s in range(target+1):
                f[0][k][s] = 0
        f[0][0][0] = 1
        f[i][j][s] = f[i-1][j][s] + f[i-1][j-1][s-nums[j]]

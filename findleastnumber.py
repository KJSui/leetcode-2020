class Solution:
    def findLeastNumber(self, N):
        f = [N+1 for _ in range(N+1)]
        f[0] = 0
        f[1] = 0
        for i in range(2, N+1):
            f[i] = min(f[i], f[i-1]+1)
            if i%2 == 0:
                f[i] = min(f[i], f[i/2]+1)
            if i%3 == 0:
                f[i] = min(f[i], f[i/3]+1)
        print("f:", f)
        return f[N]

obj = Solution()
N = 11
print(obj.findLeastNumber(N))

'''
给一个N， n>0, 可以有三种 Operation, n-1, n/2, n/3, 但是可以进行除法的时候必须余数为0. 求最少几次运算可以到1， 然后优化。
'''
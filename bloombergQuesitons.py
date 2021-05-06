class Solution:
    def TakeNToOne(self, n):
        step = 0
        self.mp = {}
        if n%2:
            n = 3 * n + 1
            step += 1
        return self.dfs(n, step)
    def dfs(self, n, step):
        if n in self.mp:
            return self.mp[n]
        if n == 1:
            return step
        else:
            n = n//2
            k = self.dfs(n, step+1)
            self.mp[n] = k
            return k


obj = Solution()
n = 16
print(obj.TakeNToOne(n))

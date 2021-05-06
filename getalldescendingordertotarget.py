class Solution:
    def getSubsetsNumber(self, num):
        self.res = []
        self.dfs(num, [], num)
        return self.res

    def dfs(self, target, lt, start):
        if start <= 0 or target < 0:
            return
        if target == 0:
            #if sum(lt) == num:
            self.res.append(lt[:])
            return

        for i in range(start, 0, -1):
            #print("i value:", i, "target:", target, "start:", start)
            lt.append(i)
            #print("list:", lt)
            self.dfs(target-i, lt, i)
            lt.pop()

        return

    def calsum(self):
        #f[7] = f[6] * f[1] = f[5] * f[2]
        return len(self.res)

    def length(self, num):
        f = [0] * (num+1)
        f[1] = 1
        f[2] = 2
        f[3] = 3
        for i in range(4, num+1):
            f[i] = f[i-2] * f[2] + 1
        return f[num]

obj = Solution()
num = 10
print(obj.getSubsetsNumber(num))
print(obj.calsum())
print(obj.length(num))

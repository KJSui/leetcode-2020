class Solution:
    def makesquare(self, nums):
        nb = sorted(nums, reverse=True)
        totalsum = sum(nb)
        if(totalsum%4) != 0:
            return False
        sidelen = totalsum/4
        if sidelen == 0:
            return False
        self.visited = set()
        self.size = 4
        return self.dfs(nb, sidelen)
        
    def dfs(self, nb, sidelen):
        print("15 sidelen:", sidelen, "nb:", nb)
        if sidelen == 0:
            return True
        if sidelen < 0:
            return False
        for j in range(len(nb)):
            print("20 j:", j, "nb:", nb)
            if j in self.visited:
                continue
            self.visited.add(j)
            value = nb[j]
            print("25 value:", value)
            if self.dfs(nb, sidelen - value):
                self.size -= 1
                if self.size == 0:
                    return True
                continue
            self.visited.remove(j)
        return False

obj = Solution()
nums = [5,5,5,5,4,4,4,4,3,3,3,3]
print(obj.makesquare(nums))
class Solution:
    def pathsum3(self, root, sm):
        self.cache = {}
        self.res = 0
        self.dfs(root, sm, 0)
        return self.res 

    def dfs(self, root, sm, currpathsum):
        if not root:
            return
        currpathsum += root.val
        oldpathsum = currpahtsum - sum
        self.res += self.cache.get(oldpathsum, 0)
        self.cache[currpathsum] = self.cache.get(currpathsum, 0)+1
        self.dfs(root.left, sm, currpathsum)
        self.dfs(root.right, sm, currpathsum)
        self.cache[currpathsum] -= 1
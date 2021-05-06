class Solution:
    def areasOfEachIsland(self, islands):
        self.res = []
        self.visited = set([])
        self.dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        self.count = 0
        row = len(islands)
        col = len(islands[0])
        for i in range(row):
            for j in range(col):
                if islands[i][j] == 1 and (i, j) not in self.visited:
                    self.visited.add((i, j))
                    self.count = 1
                    self.dfs(islands, i, j)
                    self.res.append(self.count)
        return self.res
    def dfs(self, islands, r, c):
        for i in range(4):
            nr = self.dir[i][0] + r
            nc = self.dir[i][1] + c 
            if nr >= 0 and nr < len(islands) and nc >= 0 and nc < len(islands[0]): 
                if (nr, nc) not in self.visited:
                    self.visited.add((nr, nc))
                    if islands[nr][nc] == 1:
                        self.count += 1
                        self.dfs(islands, nr, nc)

islands = [[1, 0, 1], [1, 1, 0], [1, 0, 0]]
obj = Solution()
print(obj.areasOfEachIsland(islands))

"""
1 0 1
1 1 0
1 0 0
"""
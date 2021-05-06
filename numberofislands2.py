class UnionFind:
    def __init__(self):
        self.parent = []
        self.rank = []
        self.count = 0

    def unionFind(self, m, n, grid):
        self.parent = [-1]*m*n 
        self.rank = [0]*m*n 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i*n+j] = i*n+j 
                    self.count += 1
    
    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        ix = self.find(x)
        iy = self.find(y)

        if ix != iy:
            if self.rank[ix] < self.rank[iy]:
                self.rank[iy] = ix 
            elif self.rank[ix] > self.rank[iy]:
                self.rank[ix] = iy 
            else:
                self.rank[ix] = iy 
            self.count -= 1

    def setParent(self, i):
        self.parent[i] = 1
        self.count += 1

    def isValid(self, i):
        if self.parent[i] >= 0:
            return True 
        return False 

class Solution:
    def numIsland2(self, m, n, grid, positions):
        uf = UnionFind()
        uf.unionFind(m, n, grid)

        ans = [] 

        for pos in positions:
            first = pos[0]
            second = pos[1]
            index = first * n + second 
            overlap = []
            if (first-1) >= 0 and uf.isValid((first-1)*n+second)):
                overlap.append((first-1)*n+c) 
            if (second-1) >= 0 and uf.isValid(first*n+second-1)):
                overlap.append((first)*n+c-1)
            if (first+1) < m and uf.isValid((first+1)*n+second)):
                overlap.append((first+1)*n+c) 
            if (second+1) < m and uf.isValid(first*n+second+1)):
                overlap.append((first)*n+c+1)
            uf.setParent(index)
            for i in overlap:
                uf.union(i, index)

            ans.append(uf.count)

        return ans                                  
                


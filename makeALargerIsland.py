class Solution:

    def largestIsland(self, grid):
        N = len(grid)
        size = 2
        island_idx = {}
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    island_idx[index]=self.dfs(grid, i, j, size)
        ans = max(island_idx.values() or [0])
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 0:
                    seen = {grid[ni][nj] for ni, nj in neighbor(N, i, j) if grid[ni][nj] > 1}
                    ans = max(ans, 1+sum(island_idx[k] for k in seen))
        return ans
    def dfs(self, grid, x, y, size):
        ans = 1
        grid[x][y] = size
        for nr, nc in neighbor(len(grid), x, y):
            if grid[nr][nc] == 1:
                ans += self.dfs(grid, nr, nrc, size)
        return ans

    def neighbor(self, n, r, c):
        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if nr >= 0 and nr < n and nc >= 0 and nc < n:
                yield nr, nc

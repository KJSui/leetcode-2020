class Solution:
    def longestIncreasingPath(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        self.cache = [[0 for i in range(n)] for j in range(m)]
        self.dirc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(matrix, i, j))
        return res
    def dfs(self, matrix, i, j):
        if i < 0 or i >= m or j < 0 or j >= n:
            return 0
        if self.cache[i][j]:
            return self.cache[i][j]
        for k in self.dirc:
            ni = i + k[0]
            nj = j + k[1]
            if ni >= 0 and ni < m and nj >= 0 and nj < n and matrix[ni][nj] > matrix[i][j]:
                self.cache[i][j] =  max(self.dfs(matrix, ni, nj), self.cache[i][j])
        self.cache[i][j] += 1
        return self.cache[i][j]

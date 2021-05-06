class Solution:
    def longestIncreasingPath(self, matrix):
        if len(matrix) == 0:
            return 0

        self.cache = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

        ans = 0
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                ans = max(ans, self.dfs(matrix, i, j))
        return ans

    def dfs(self, matrix, i, j):
        if self.cache[i][j]:
            return self.cache[i][j]

        for d in self.dirs:
            x = i + d[0]
            y = j + d[1]
            if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]) and matrix[x][y] > matrix[i][j]:
                self.cache[i][j] = max(self.dfs(matrix, x, y), self.cache[i][j])

        self.cache[i][j] += 1
        return self.cache[i][j] 
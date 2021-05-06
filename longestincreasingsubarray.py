class Solution:
    def findlongest(self, matrix):
        res = 0
        self.flag = self.dp = [[0]*len(matrix[0])]*len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dp[i][j] = self.search(i, j, matrix)
                res = max(res, self.dp[i][j])
        return res
    
    def search(self, x, y, matrix):
        if self.flag[x][y] != 0:
            return self.dp[x][y]
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        n = len(matrix)
        m = len(matrix[0])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if matrix[x][y] > matrix[nx][ny]: 
                    ans = max(ans, self.search(nx, ny, A)+1)
            
        self.flag[x][y] = 1
        self.dp[x][y] = ans 
        return ans 
class Solution:
    def findoneboundaryzero(self, matrix):
        self.mp = {}
        self.dirc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] > 0:
                    depth = self.bfs(matrix, i, j)
                    matrix[i][j] = depth
                    self.mp[(i, j)] = depth
        return matrix
    def bfs(self, matrix, x, y):
        m = len(matrix)
        n = len(matrix[0])
        queue = [[x, y, 0]]
        currlen = float('inf')
        while queue:
            x, y, depth = queue.pop(0)
            for d in self.dirc:
                nx, ny = d[0] + x, d[1] + y
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
            
                if (nx, ny) in self.mp:
                    if self.mp[(nx, ny)] > currlen:
                        continue
                    else:
                        currlen = min(self.mp[(nx, ny)] + 1, currlen)
                else:
                    if matrix[nx][ny] > 0:
                        if depth + 1 > currlen:
                            continue
                        queue.append([nx, ny, depth+1])
                    else:
                        currlen = min(currlen, depth+1)
        return currlen

obj = Solution()
matrix  =[[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0], [1, 1, 1, 0]]
print(obj.findoneboundaryzero(matrix))
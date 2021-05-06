class Cell:
    def __init__(self, xx, yy, hh):
        self.x = xx
        self.y = yy
        self.h = hh

class Solution:
    def trapRainWater(heights):
        if len(heights) == 0:
            return 0

        heap = []
        n = len(heights)
        m = len(heights[0])
        visit = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            heapq.heappush(visit, Cell(i, 0, heights[i][0]))
            heapq.heappush(visit, Cell(i, m-1, heights[i][m-1]))
            visit[i][0] = 1
            visit[i][m-1] = 1
        for j in range(m):
            heapq.heappush(visit, Cell(0, j, heights[0][j]))
            heapq.heappush(visit, Cell(n-1, j, heights[n-1][j]))
            visit[0][j] = 1
            visit[n-1][j] = 1

        ans = 0
        while len(q):
            now = q.pop()
            for i in range(4):
                nx = dp[i] + now.x
                ny = dy[i] + now.y
                if visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    heapq.heapush(heap, Cell(nx, ny, max(now.h, heights[nx][ny])))
                    ans = ans + max(0, now.h - heights[nx][ny])

        return ans 

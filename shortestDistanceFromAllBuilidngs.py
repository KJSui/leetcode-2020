class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        target = 0
        dist = [[0 for j in range(n)] for i in range(m)]
        dirc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        mindist = float('inf')

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q = [[i, j]]
                    level = 1
                    while len(q):
                        size = len(q)
                        while size > 0:
                            node = q.pop(0)
                            for k in range(4):
                                x = node[0] + dirc[k][0]
                                y = node[1] + dirc[k][1]
                                if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == target:
                                    grid[x][y] -= 1
                                    dist[x][y] += level
                                    q.append([x, y])
                            size -= 1
                        level += 1
                    target -= 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == target:
                    mindist = min(mindist, dist[i][j])
        return mindist if mindist != float('inf') else -1 

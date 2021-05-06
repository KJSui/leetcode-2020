class Solution:
    def __init__(self):
        self.queue = []
        self.visited = set()

    def numberIslands(self, grid):
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in self.visited:
                    continue
                self.visited.add((i, j))
                if grid[i][j] is '1':
                    self.check(grid, i, j)
                    res += 1
                    self.queue = []

        return res

    def check(self, grid, row, col):
        self.queue.append([row, col])
        while len(self.queue):
            curr = self.queue.pop(0)
            row = curr[0]
            col = curr[1]

            if row > 0 and row < len(grid)-1:
                self.verify(grid, row+1, col)
                self.verify(grid, row-1, col)

            if col > 0 and col < len(grid[0])-1:
                self.verify(grid, row, col+1)
                self.verify(grid, row, col-1)

            if row == 0 and row < len(grid)-1:
                self.verify(grid, row+1, col)

            if row > 0 and row == len(grid)-1:
                self.verify(grid, row-1, col)

            if col == 0 and col < len(grid[0])-1:
                self.verify(grid, row, col+1)

            if col > 0 and col == len(grid[0])-1:
                self.verify(grid, row, col-1)

    def verify(self, gird, row, col):
        if (row, col) not in self.visited:
            self.visited.add((row, col))
            if gird[row][col] == 1:
                self.queue.append([row, col])
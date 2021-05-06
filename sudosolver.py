from collections import defaultdict
class Solution:
    def sudoSolver(self, board):
        self.rows = [defaultdict(int) for i in range(9)]
        self.cols = [defaultdict(int) for i in range(9)]
        self.boxers = [defaultdict(int) for i in range(9)]
        self.box_index = lambda row, col: (row//3)*3 + col//3
        self.solved = False
    def backtrack(self, row, col, board):
        if board[row][col] == ".":
            for d in range(1, 10):
                if self.could_add(d, row, col):
                    self.place_num(d, row, col)
                    self.place_next_num(d, row, col)
                    if not self.solved:
                        self.remove_num(d, row, col)

        else:
            self.place_next_num(d, row, col)

    def could_add(self, d, row, col):
        return not (d in self.rows[row] or d in self.cols[col] or d in self.boxers[self.box_index(row, col)])
    def place_num(self, d, row, col):
        
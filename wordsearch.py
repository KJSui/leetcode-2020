class Solution:
    def wordSearch(self, board, word):
        rowl = len(board)
        coll = len(board[0])
        self.visited = [[0 for i in range(coll)] * for j in range(rowl)]

        self.dict = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(rowl):
            for j in range(coll):
                if self.dfs(board, word, board[0][0], i, j):
                    return True 
        return False 

    def dfs(self, board, word, tmp, i, j):
        if self.visited[i][j]:
            return False 
        if tmp == word:
            return True 
        if len(tmp) == len(word):
            return False
        if tmp != word[:len(tmp)]:
            return False 
        self.visited[i][j] = 1
        for k in range(4):
            newRow = i + self.dict[k][0]
            newCol = j + self.dict[k][1]
            if newRow >= 0 and newRow < len(board) and newCol >= 0 and newCol < len(board[0]):
                if self.dfs(board, word, tmp+board[newRow][newCol], newRow, newCol):
                    return True 
        self.visited[i][j] = 0
        return False 


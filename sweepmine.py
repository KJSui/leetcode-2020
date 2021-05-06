class Solution:
    def updateBoard(self, board, click):
        if board[click[0][click[1]]] == "M":
            board[click[0][click[1]]] = "X"
            return board 

        queue = []
        dirctions = [[1, 0], [0, 1],[-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        queue.append(click)

        while queue:
            dot = queue.pop(0)
            tmpq = []
            ctrl = 0
            for i in dirctions:
                newX = dot[0]+i[0]
                newY = dot[1]+i[1]
                if newX >= 0 and newX <= len(board) and newY >= 0 and newY <= len(board[0]):
                    if board[newX][newY] == "E":
                        tmpq.append([newX, newY])
                        elif board[newX][newY] == "M":
                            ctrl += 1
            
            if ctrl == 0:
                board[click[0]][click[1]] = "B"
                while len(tmpq) > 0:
                    v = tmpq.pop(0)
                    board[v[0]][v[1]] = "#"
                    queue.append(v)
            else:
                board[click[0]][click[1]] = str(ctrl)

        return board
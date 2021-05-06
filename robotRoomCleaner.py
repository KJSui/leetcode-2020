class Solution:
    def cleanRoom(self, robot):
        directions = [(-1, 0), (1, 0), (0, 1), (0,-1)]
        visited = set()

        def backtrack(cell = (0, 0), dir = 0):
            visited.add(cell)
            robot.clean()
            for i in range(4):
                new_dir = (i+dir)%4
                new_cell = (cell[0]+directions[new_dir][0], cell[1]+directions[new_dir][1])
                if new_cell not in visited and robot.move():
                    backtrack(new_cell, new_dir)
                    go_back()

                robot.turnRight()
            
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()


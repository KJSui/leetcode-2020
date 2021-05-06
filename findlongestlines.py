class Solution:

    def findlongestline(self, array):
        row = len(array)
        col = len(array[0])
        res = 0
        d = [[[0, 0, 0]] * (col)] * (row)
        queue = []
        v = [1, 1, 1] if array[0][0] == 1 else [0, 0, 0]
        queue.append([0, 0, v])
        while len(queue) > 0:
            curr = len(queue)
            while curr > 0:
                r, c, v = curr.pop(0)
                if r + 1 < row:
                    if array[r+1][c] == 1:
                        v[0] += 1
                        v[1] = max(v[1], 1)
                    else:
                        v[0] = 0
                
        for i in range((row)):
            for j in range((col)):
                if i == 0 and j == 0:
                     d[i][j] = [1, 1, 1] if array[i][j] == 1 else [0, 0, 0]
                elif i == 0 and j != 0:
                    d[i][j][0] = d[i][j-1][0] + 1 if array[i][j] == 1 else 0
                elif i != 0 and j == 0:
                    d[i][j][1] = d[i-1][j][1] + 1 if array[i][j] == 1 else 0
                else:   
                    if d[i][j] == 1:
                        d[i][j][0] = d[i][j-1][0] + 1
                        d[i][j][1] = d[i-1][j][1]+ 1
                        d[i][j][2] = d[i-1][j-1][2] +1
                    else:
                        d[i][j] = [0, 0, 0]
                print("d[i-1][j-1]:", d[i][j])
                res = max(res, max(d[i][j]))

        return res

obj = Solution()
array = [   [1, 1, 1, 0], 
            [1, 1, 0, 1], 
            [0, 1, 1, 1],
            [0, 0, 1, 1]
        ]
print(obj.findlongestline(array))
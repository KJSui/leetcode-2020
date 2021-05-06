class Solution:
    def triaggle(self, triag):
        rowLength = len(triag)
        for i in range(rowLength-2, -1, -1):
            for j in range(i+1):
                triag[i][j] += min(triag[i+1][j], triag[i+1][j+1])
                if triag[i+1][j] < triag[i+1][j+1]:
                    print("row: ", i, "col: ", j, "value: ", triag[i+1][j])
                else:
                    print("row: ", i, "col: ", j, "value: ", triag[i+1][j+1])

        return triag[0][0]

obj = Solution()
triag = [[2], [3, 4], [6,5,7], [4,1,8,3]]

print(obj.triaggle(triag))


class Solution:
    def spiralOrder(self, m, n):
        row_l = m
        col_l = n

        self.res = [[' ' for i in range(n)] for j in range(m)]
        i = 0
        j = 0
        while i < row_l and j < col_l:
            self.iterator(i, j, row_l-i, col_l-j)
            i += 2
            j += 2

        return self.res


    def iterator(self, r, c, rl, cl):
        orig_r = r
        orig_c = c

        while r < rl:
            self.res[r][c] = '1'
            r += 1
        r -= 1
        c += 1

        while c < cl:
            self.res[r][c] = '1'
            c += 1
        c -= 1
        r -= 1

        while r >= orig_r+2:
            self.res[r][c] = '1'
            r -= 1

        r += 1
        c -= 1
        while c >= orig_c+2:
            self.res[r][c] = '1'
            c -= 1
obj = Solution()
res = (obj.spiralOrder(10, 10))

for i in range(10):
    print(res[i])

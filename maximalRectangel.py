class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or len(matrix) == 0:
            return 0

        n = len(matrix[0])
        height = [0] * (n+1)
        ans = 0
        for row in matrix:
            for i in range(n):
                height[i] += 1 if row[i] == '1' else 0
            
            stack = [-1]
            for i in range(n+1):
                while height[i] < height[stack[-1]]:
                    k = stack.pop()
                    w = i - 1 - stack[-1]
                    ans = max(ans, w * height[k])
                stack.append(i)
        return ans
                
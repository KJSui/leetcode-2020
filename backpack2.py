"""
There are n items and a backpack with size m. Given array A representing the size of each item and array V representing the value of each item.

What's the maximum value can you put into the backpack?
"""

class Solution:
    def backpack2(self, n, A, W, V):
        f = [[-1]*(w+1) for i in range(n+1)]
        for i in range(1, n+1):
            w = W
            while w >= 0:
                if w >= A[i-1] and f[i-1][w-A[i-1]] != -1:
                    f[i][w] = max(f[i-1][w], f[i-1][w-A[i-1]]+V[i-1])
                w -= 1
            
"""
 可以放无线个对于一个物品
“”“

for i in range(n+1):
    for w in range(m, -1, -1):
        while w >= k*A[i-1]:
            f[i][w] = max( f[i-1][w-kA[i-1]]+kA[i-1])


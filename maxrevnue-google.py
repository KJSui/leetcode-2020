f[n][0] = max(f[n-1][0] + A[n-1], f[n-1][1] + B[n-1] - cost[BA])

class Solution:
    def cheapestJump(A, B):
        f = [0] * len(A)
        next = [-1] * len(A)

        for i in range(len(A)-2, -1, -1):
            mincost = float('inf')
            for j in range(i+1, min(i+B+1, len(A))):
                    if A[j] >= 0:
                        cost = A[j] + f[j]
                        if cost < mincost:
                            mincost = cost
                            next[i] = j
            f[i] = mincost

        i = 0
        res = []
        while i < len(A) and next[i] > 0:
            res.append(i+1)
            i = next[i]

        if i == len(A)-1 and A[i] >= 0:
            res.append(len(A))
        else:
            return []

        return res

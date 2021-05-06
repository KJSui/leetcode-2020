class solution：
    def paintHouse2(self, A):
        n = len(A)
        k = len(A[0])
        m = [[0]*(k) for _ in range(m+1)]
        for i in range(k):
            m[0][k] = 0
        m1 = m2 = float('inf')
        for i in range(1, len(A)):
            j1 = j2 = 0
            for j in range(len(A[0])):
                if m[i-1][j] < min1:
                    min2 = min1
                    j2 = j1
                    min1 = m[i-1][j]
                    j1 = j
                elif m[i-1][j] < min2:
                    min2 = m[i-1][j]
                    j2 = j

            for j in range(k):
                if j != j1:
                    m[i][j] = m[i-1][j1]+A[i-1][j]
                elif j = j2:
                    m[i][j] = m[i-1][j2] + A[i-1][j]


        res = float('inf')
        for i in range(k):
            res = min(res, m[n][i])
        return res


def painthosue2(self, A):
    m = [[0] * (len(A[0])) for i in range(len(A)+1)]
    for i in range(len(A[0])):
        f[0][i] = 0

    for i in range(1, len(A)+1):
        min1 = min2 = float('inf')
        fo j in range(len(A[0])):
            if m[i-1][j] < min1:
                min2 = min1
                j2 = j1
                j = j
                min1 = m[i-1][j]
            elif m[i-1][j] < min2:
                min2 = m[i-1][j]
                j2 = j

        for j in range(len(A[0])):
            if j != j1:
                m[i][j] = (m[i-1][j1] + cost[i-1][j])
            else:
                m[i][j] = m[i-1][j2] + cost[i-1][j]

    res = float('inf')
    for k in range(len(A[0])):
        res = min(res, m[n][k])
    return res
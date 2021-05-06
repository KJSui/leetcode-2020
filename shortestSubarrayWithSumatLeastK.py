class Soltution:
    def shortestSubarray(self, A, K):
        N= len(A)
        p = [0]
        for x in A:
            p.append(P[-1]+x)

        ans = N+1
        dq = collections.deque()
        for y, py in enumerate(P):
            while dq and p[dq[-1]] >= py:
                dq.pop()

            while dq and py - p[dq[0]] >= K:
                ans = min(ans, y - dq.popleft())

            dq.append(y)

        return ans if asn < N+1 else -1
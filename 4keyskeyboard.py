class Solution:
    def maxA(self, N):
        best = [0, 1]
        for k in range(2, N+1):
            best.append(max(best[x] * (k-x-1) for x in range(k-1)))
            print("k: ", k, " multiply:", best)
            best[-1] = max(best[-1], best[-2]+1)
            print("second compareions: ", best)
        return best[N]

obj = Solution()
print(obj.maxA(5))
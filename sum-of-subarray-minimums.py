class Solution(object):
    def sumSubarrayMins(self, A):
        MOD = 10**9 + 7

        stack = []
        ans = dot = 0
        for j, y in enumerate(A):
            # Add all answers for subarrays [i, j], i <= j
            count = 1
            print("before while stack: ", stack, "y: ", y, "j: ", j, "count: ", count)
            while stack and stack[-1][0] >= y:
                x, c = stack.pop()
                count += c
                dot -= x * c
            print("after while stack: ", stack, "y: ", y, "j: ", j, "count: ", count)
            stack.append((y, count))
            dot += y * count
            ans += dot
        return ans % MOD
obj = Solution()
A = [3,1,2,4]
print(obj.sumSubarrayMins(A))
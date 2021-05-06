class Solution:
    def sumSubarrayMins(self, A):
        MOD = 10 ** 9 + 7
        
        stack = []
        ans = dot = 0
        for j, y in enumerate(A):
            count = 1
            while stack and stack[-1][0] >= y:
                x, c = stack.pop()
                count += c
                dot -= x * c
                
            stack.append((y, count))
            print("stack: ", stack)
            dot += y * count
            ans += dot
            
        return ans % MOD

obj = Solution()
A = [4, 2, 1]
print(obj.sumSubarrayMins(A))
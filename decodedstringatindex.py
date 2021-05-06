class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        size  = 0
        for c in S:
            if c.isdigit():
                size += int(c)
            else:
                size += 1
        print("size: ", size)      
        for c in reversed(S):
            K %= size
            if K == 0 and c.isalpha():
                return c
            
            if c.isdigit():
                size = int(size/int(c))
                print("digital size: ", size, "digit: ", c)
            else:
                size -= 1
                print("alpha size: ", size, "digit: ", c)
                
obj = Solution()
S = "leet2code3"
K = 10
print(obj.decodeAtIndex(S, K))
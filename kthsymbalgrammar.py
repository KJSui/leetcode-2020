class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        self.res = ""
        self.helper(N)
        print("res: ", self.res)
        return int(self.res[K-1])
        
    
    def helper(self, N):
        if N == 0:
            return
        if N == 1:
            self.res = "0"
        self.helper(N-1)
        i = 0
        length = len(self.res)
        while i < length*2:
            k = self.res[i]
            if k is "0":
                self.res = self.res[:i] + "01"+self.res[i+1:]
            else:
                self.res = self.res[:i]+"10"+self.res[i+1:]
            i += 2
        print("the ", i, "th res: ", self.res)
        return
            
obj = Solution()
print(obj.kthGrammar(3, 3))


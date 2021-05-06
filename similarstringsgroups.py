class Solution:
    def numSimilarGroups(self, A):
        self.st = set()
        for word in range(0, len(A)):
            self.st.add(A[word])
        
        queue = []
        res = 0
        while len(self.st) > 0:
            queue.append(self.st.pop())
            while queue:
                w = queue.pop(0)
                i = 0
                for i in range(len(w)):
                    j = len(w)-1
                    while i < j:
                        print("15 word:", w)
                        newword = w[:i] + w[j] + w[i+1:j] + w[i] + w[j+1:]
                        print("16:newword:", newword)
                        print("17 set:", self.st)
                        if newword in self.st:
                            queue.append(newword)
                            self.st.remove(newword)
                        print("20:queue:", queue)
                        j -= 1
            res += 1
            print("24 set:", self.st)       
        return res
            
A = ["tars","rats","arts","star"]
obj = Solution()
print(obj.numSimilarGroups(A))

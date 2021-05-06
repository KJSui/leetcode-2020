class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        res = S[:]
        #indexes.sort()
        print("S:", S, "indexes:", indexes, "sources: ", sources, "targets:", targets)
        count = 0
        mp = {}
        for i, v in enumerate(indexes):
            mp[v] = i
        indexes.sort()
        for j in range(len(indexes)):
            index = indexes[j]
            i = mp[index]
            print("index:",index, "i: ", i, "sources[i]:", sources[i], "S[index:len(sources[i])]:", S[index:index + len(sources[i])])
            if S[index:index + len(sources[i])] == sources[i]:
                res = res[:count + index] + targets[i] + res[count + index + len(sources[i]):]
                count += len(targets[i])- len(sources[i])
                print("res:", res, "count:", count, "\n")
        
                
        return res 
obj = Solution()
S = "vmokgggqzp"
indexes = [3,5,1]
sources = ["kg","ggq","mo"]
targets = ["s","so","bfr"]
print(obj.findReplaceString(S, indexes, sources, targets))

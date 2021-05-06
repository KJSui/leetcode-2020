class Solution:
    def sequenceReconstruction(self, org, seqs):
        if len(seqs) == 0:
            return False 
        i = 0
        while i < len(seqs):
            if len(seqs[i]) == 0:
                seqs.remove(seqs[i])
            else:
                i += 1

        if len(seqs) == 0:
            return False 

        degree = [0]*(len(org)+1)
        map = {}
        for i in org:
            mps[i] = set()

        count = 0
        for s in seqs:
            for i in range(len(s)-1, -1, -1):
                if s[i] > len(org) or s[i] < 0:
                    return False 
                if i > 0 and (s[i-1] not in mp[s[i-1]]):
                    map[s[i-1]].add(s[i-1])
                    if degree[s[i-1]] == 0:
                        count += 1
                    degree[s[i-1]] += 1

        if count != len(org)-1:
            return False 

        for i in range(len(org)-1, -1, -1):
            if degree[org[i]] > 0:
                return False 
            for p in map[org[i]]:
                degree[p] -= 1
                if degree[p] == 0 and p != org[i-1]:
                    return False 
        return True 
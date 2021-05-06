import collections
class Solution:
    def findRelationship(self, relations, n1, n2):
        mp = collections.defaultdict(map)
        for i in relations:
            if i[0] not in mp:
                mp[i[0]] = {i[2]:[i[1]]}
            else:
                if i[2] not in mp[i[0]]:
                    mp[i[0]][i[2]] = [i[1]]
                else:
                    if i[1] not in mp[i[0]][i[2]]:
                        mp[i[0]][i[2]].append(i[1])
        print("mp: ", mp)
        print("")
        self.res = []
        self.bfs(mp, n1, n2, [])
        return self.res

    def bfs(self, mp, n1, n2, crrList):
        if n1 == n2:
            self.res.append(crrList[:])
            return
        if n1 in mp.keys():
            for i in mp[n1].keys():
                mp[n1][i] = [i] + mp[n1][i]
                self.bfs(mp, i, n2, crrList + mp[n1][i])
                mp[n1][i] = mp[n1][i][1:]
        return

obj = Solution()
relations = [['Bart', 'brother', 'Lisa'], ['Bart', 'son', 'Homer'], ['Marge', 'wife', 'Homer'], ['Lisa', 'daughter', 'Homer']]

print(obj.findRelationship(relations, 'Bart', 'Homer'))
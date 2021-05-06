from collections import defaultdict
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.map = defaultdict(set)

    def unionInit(self, mp):
        for word in mp:
            self.parent[word[0]] = word[0]
            self.parent[word[1]] = word[1]
    def find(self, x):
        #print("self.parent[x]:", self.parent[x])
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x1 = self.find(x)
        y1 = self.find(y)
        if x1 != y1:
            self.parent[y1] = x1
        if x1 not in self.map:
            self.map[x1].add(x1)
        self.map[x1].add(x)
        self.map[x1].add(y)

    def search(self, x):
        if x in self.map.keys():
            return self.map[x]
        else:
            return {}

class Solution:
    def findAllCombination(self, mp, words):
        self.uf = UnionFind()
        self.uf.unionInit(mp)
        for word in mp:
            self.uf.union(word[0], word[1])
        self.res = []
        self.visited = set()
        self.backtracking(words, 0)
        return self.res
    def backtracking(self, words, idx):
        if idx == len(words):
            return
        lt = self.uf.search(words[idx])
        if len(lt) > 0:
            for j in lt:
                tmp = words[:idx] + [j] + words[idx+1:]
                str_tmp = " ".join(tmp)
                if str_tmp not in self.visited:
                    self.res.append(str_tmp[:])
                    self.visited.add(str_tmp)
                else:
                    continue
                self.backtracking(tmp, idx+1)
        else:
            self.backtracking(words, idx+1)


obj = Solution()
words = ["I", "love", "a",  "JOY"]
mp = [["love", "like"], ["like", "favor"], ["JOY", "Happy"]]
print(obj.findAllCombination(mp, words))
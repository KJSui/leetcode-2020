class DSU:
    def __init__(self):
        self.p = range(10001)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)

class Solution:
    def accountsMerge(self, accounts):
        dsu = DSU()
        em_to_name = {}
        em_to_id = {}
        i = 0
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                em_to_name[email] = name
                if email not in em_to_id:
                    em_to_id[email] = i
                    i += 1
                dsu.union(em_to_id[account[1]], email)
        ans = collecitons.defaultdict(list)
        for email in em_to_name.keys():
            ans[dsu.find(em_to_id[email])].append(email)
        return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]
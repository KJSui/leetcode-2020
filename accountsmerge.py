def DSU:
    def __init__(self):
        self.root = {}
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        self.root[self.find[x]] = self.find[y]

    
class Solution:
    def mergeAccount(self, accounts):
        email_to_id = {}
        email_to_name = {}
        i = 0
        dsu = DSU()

        for ac in accounts:
            name = ac[0]
            for em in accounts[1:]:
                email_to_name[em] = name 
                if em not in email_to_id:
                    email_to_id[em] = i 
                    i += 1
                dsu.union(email_to_id[accounts[1]], email_to_id[em])

        ans = collections.defaultdict(list)
        for i in email_to_name.keys():
            ans[dsu.find(email_to_id[i])].append(i)
        return [[email_to_name[v[0]]] + sorted(v) for v in ans.values()


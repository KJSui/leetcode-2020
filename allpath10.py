class Solution:
    def allpath(self, list):
        self.res = []
        self.dfs("", list, 0)
        return self.res

    def dfs(self, path, list, idx):
            if idx == len(list):
                self.res.append(path)
                return
            if list[idx] == '?':
                for i in range(0,2):
                    self.dfs(path + str(i), list, idx+1)
            else:
                self.dfs(path+str(list[idx]), list, idx+1)
            return
obj = Solution()
list = [1, '?', 0, '?', 1]
print(obj.allpath(list))

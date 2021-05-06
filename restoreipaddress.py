class Solution:
    def restoreIpAddresses(self, s):
        self.res = []
        self.dfs(s, 0,  0, "")
        return self.res
    def valid(self, segment):
        return int(segment) <= 255 if segment[0] != "0" else len(segment) == 1
  
    def dfs(self, s, pos, count, tmp):
        if count == 4 and pos == len(s):
            self.res.append(tmp[:-1])
            return
        if count > 4:
            return
        print("tmp: ", tmp)
        for i in range(1, 4):
            if pos+i > len(s):
                break
            segment = s[pos:pos+i]
            if not self.valid(segment):
                continue
            
            self.dfs(s, pos+i, count+1, tmp+segment+".")
                
obj = Solution()
s = "25525511135"
print(obj.restoreIpAddresses(s))

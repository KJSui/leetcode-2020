class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        st = {}
        tmp = {}
        res = []
        counter = len(p)
        for i in p:
            if i not in st:
                st[i] = 1
            else:
                st[i] += 1
        
        tmp = st.copy() 
        i = 0
        while i < len(s):
            if s[i] in tmp:
                tmp[s[i]] -= 1
                counter -= 1
                if tmp[s[i]] == 0:
                    del tmp[s[i]]
                    if len(tmp) == 0:
                        res.append(i-len(p)+1)
                        tmp = st.copy()
                        counter = len(p)
                        i = i - len(p) + 2
                        continue
                i += 1
                print("in i: ", i, "res: ", res, "tmp: ", tmp)
            else:
                i = i - (len(p)-counter) + 1
                tmp = st.copy()
                counter = len(p)
                print("out i: ", i, "res: ", res, "tmp: ", tmp)

        return res
                
obj = Solution()
s = "abacbabc"
p = "abc"
print(obj.findAnagrams(s, p))
class Solution:
    def twoStringCompare(self, s1, s2):
        self.mp2 = defaultdict(list)
        self.mp1 = defaultdict(list)
        ans1 = [s1]
        ans2 = [s2]
        return self.rec(ans1, ans2, 0)


    def self.rec(self, ans1, ans2, k):
        if len(ans1) != len(ans2):
            return False 
        if k == len(ans1):
            return True 
        for k in range(len(ans1)):
            ans1 = self.getinterval(ans1[k], self.mp1)
            ans2 = self.getinterval(ans2[k], self.mp2)
            if s1[0] != s2[0]:
                return False 
            if s1[0] == "[":
                if(self.cmp(ans1, ans2, 1) == False):
                    return False 
            else:
                if(self.cmp(ans1, ans2, 0)== False):
                    return False 
            return self.rec(ans1, ans2, k)
        

    def getinterval(self, s, mp):
        ans = []
        i = 1
        num = 1 if s[0] == "[" else 2
        while i < len(s):
            stack = []
            start = 0
            stack.append(s[start])            
            while len(stack) > 0:
                if s[i] is "[":
                    stack.append(s[i])
                    num = num * 10 + 1
                elif s[i] is "{":
                    stack.append(s[i])
                    num = num * 10 + 2
                elif s[i] is "}":
                    stack.pop()
                    num = num * 10 + 4
                else:
                    stack.pop()
                    num = num * 10 + 3
                i += 1
            ans.append(s[start:i])
            mp[len(s[start:i])].append(s[start:i])
            start = i 

        return ans

    def cmp(self, l1, l2, flag):
        #total length
        if len(l1) != len(l2):
                return False 
        # different category length
        if len(self.mp1.keys()) != len(self.mp2.keys()):
            return False 
        # categories length
        for i in self.mp1.keys():
            if i not in self.mp2.keys():
                return False 
            if len(self.mp1[i]) != len(self.mp2[i]):
                return False 

        if flag == 0:
            for i in self.mp1[4]:
                if i not self.mp2[4]:
                    return False 
                self.mp2[4].remove(i)
            if len(self.mp2[4]) > 0:
                return False 
            
        else:
            i = 0
            while i < len(l1):
                if len(l1[i]) != len(l2[i]):
                    return False 
                if l1[i][0] != l2[i][0]:
                    return False 
                if len(l1[i]) == 2:
                    l1[i].pop()
                if len(l1[i]) == 4:
                    if l1[i][1] != l2[i][1]:
                        return False 
                i += 1
        self.mp1 = {}
        self.mp2 = {}

        return True 
            
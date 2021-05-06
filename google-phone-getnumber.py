'''
给定一个全都是正数的数组，可以从左端或者右端取出数字，一共可以取出k次，问取出的数字和最大是多少？


我的做法是建两个长度为k的数组，分别存前缀和prefix_sum和后缀和suffix_sum。
然后遍历i in [0,k) , 取prefix_sum[k], suffix_sum[k]和prefix_sum+suffix_sum[k-i-1]中最大值。时空复杂度都为O(k)

Follow up:
再给一个长度为k的正数数组，取出来的数字依次与数组中的数字相乘，问乘积和最大是多少？
例如：原数组是[1,8,3,5,6,7,8],k=3,被乘的数组为[1,2,3]
其中一种取法是左右左，得到的乘积和就是1*1+8*2+8*3


我的做法是记忆化深搜，时空复杂度是O(k^2)
'''
import collections
class Solution:
    def getMaxNumber(self, orig, target, k):


        self.mp = set()
        self.lt = []
        self.res = 0

    def dfs(self, orig, target, k, start, end, left, tmp):
        if k == 0:
            f = self.getvalue(tmp, target)
            if self.res <= f:
                self.res = f
                self.lt.append(tmp)
            return
        
        if start in self.mp:
                return
            self.mp.add(start)
            self.dfs(orig[1:], target, k-1, tmp + orig[0])

        else:
            self.dfs(orig[:-2], target, k-1,  tmp+orig[-1])
            tmp.pop()
        return

    def getvalue(self, orig, target):
        final = 0
        for i in range(len(target)):
            final += orig[i] * target[i]
        return final
                    

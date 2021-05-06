'''
xxxxx在偶数轮可以滚落1, 3或者4个stairs，奇数轮可以滚1, 2或者4 stairs，然后中间会有一些sticky stairs，掉到sticky stairs的时候不能move小球直接挂掉。问的是从这个n个stairs高的楼梯，小球有多少种方法能够到达ground，也就是stair为0的这一层，超过的话，比如-3，-2，-1也算是到达ground。一开始用dfs的暴力解，后面想用dp做，做到一半的时候时间没了。画了个图，大概长这样。
(B)
--+
3 |
  +--+
   2 |
     +--+
      1 |
--------+---------

用dp做，但我用dfs的暴力解，最后要用dp做的时候时间不够了。
'''

class Solution:
    def methodsballsout(self, n):
        self.odd = [1, 2, 4]
        self.even = [1, 3, 4]
        self.stickystairs = set([12, 13, 34])

    def bfs(n, odd):
        if n <= 0:
            return 1 
        if n in self.memcache.keys():
            return self.memcache[n][odd]
        if n in self.stickystairs:
            return 0
        if odd:
            tmpnum = 0
            for i in self.odd:
                if self.bfs(n-i, 0):
                    tmpnum += 1
            self.memcache[n][odd] = tmpnum
        else:
            tmpnum = 0
            for i in self.even:
                if self.bfs(n-i, 1):
                    tmpnum += 1 
            self.memcache[n][odd] = tmpnum
        
        return self.memcache[n][odd]
            

dp[i] = dp[i-1][odd] + 
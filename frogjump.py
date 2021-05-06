class Solution:
    def frogJump(self, stones):
        mp  = {}
        for i in stones:
            mp[i] = set()

        mp[stones[0]].add(stones[0])

        for j in stones:
            for k in stones[j]:
                for step in range(k-1, k+2):
                    if step+k in mp:
                        mp[step+k].add(step)

        if len(mp[stones[-1]]) > 0:
            return True
        return False






                
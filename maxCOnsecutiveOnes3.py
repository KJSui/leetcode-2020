class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        res = 0
        i = 0
        end = 0
        l = K
        tmp = 0
        while i < len(A):
            while end < len(A) and l > 0:
                if A[end] == 0:
                    l -= 1
                    tmp += 1
                else:
                    tmp += 1
                res = max(res, tmp)
                end += 1
                print("tmp: ", tmp, "i: ", i, "end: ", end, "res: ", res, "l: ", l)

            while end < len(A) and A[end] == 1:
                tmp += 1
                res = max(res, tmp)
                end += 1

            if end == len(A):
                return res
            if A[i] == 0:
                l += 1
                tmp -= 1
                i += 1
            else:
                tmp -= 1
                i += 1
        return res
                

obj = Solution()
A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
K = 3
print(obj.longestOnes(A, K))
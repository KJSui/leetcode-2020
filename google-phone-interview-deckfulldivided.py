class Solution:
    def determine(self, arr):
        mp = {}
        for i in arr:
            mp[i] = mp.get(i, 0) + 1
        
        return self.helper(arr, 0, mp)

    def helper(self, arr, pos, mp):
        if pos == len(arr):
            return True
        curr = arr[pos]
        for k in range(3, len(mp.keys())):
            cp = mp.copy()
            for i in range(curr, curr+k):
                if i not in cp:
                    return False
                if cp[i] == 0:
                    return False
                cp[i] -= 1

            while pos < len(arr) and cp[arr[pos]] == 0:
                pos += 1
            if self.helper(arr, pos, cp):
                return True
        
        return False

obj = Solution()
arr = [1,2, 3, 4, 4, 5, 6]
print(obj.determine(arr))


#Define X-Straight as X cards with consecutive numbers (X >= 3). Determine if the deck can be fully divided into sets of X-Straight
#Example: 1, 2, 3, 4, 4, 5, 6 -> True
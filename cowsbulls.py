import collections
class Solution:
    def getHint(self, secret, guess):
        mp = collections.defaultdict(list)
        for i in range(len(secret)):
            mp[secret[i]].append(i)
        res = ""
        bull = 0
        cow = 0
        for i in range(len(guess)):
            if guess[i] in mp:
                lt = mp[guess[i]]
                if self.bst(lt, 0, len(lt)-1, i):
                    bull += 1
                else:
                    cow += 1
        res = str(bull)+"A" + str(cow) + "B"
        return res
        
    def bst(self, lt, left, right, target):
        if left > right:
            False
        mid = left + int((right-left)/2)
        print("mid:", mid, "left:", left, "right:", right)
        if lt[mid] == target:
            return True
        if lt[mid] < target:
            return self.bst(lt, mid+1, right, target)
        else:
            return self.bst(lt, left, mid, target)
        return False

obj = Solution()
secret = "1807"
guess = "7810"
print(obj.getHint(secret, guess))
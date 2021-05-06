class Solution:
    def recurringNumber(self, a, b):
        digit = a//b
        remain = a%b
        mp = {}
        res = str(digit)+"."
        while True:
            remain = remain * 10
            digit = remain//b
            if digit in mp:
                location = mp[digit]
                res = res[:location] + '(' + res[location:]+')'
                break
            else:
                res += str(digit)
                remain = remain%b
            mp[digit] = len(res)-1
        return res
obj = Solution()
print(obj.recurringNumber(1, 11))

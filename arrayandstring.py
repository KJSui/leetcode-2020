class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        digit = [0]*(l1+l2)
        i = len(num1)-1
        j = len(num2)-1
        while i >= 0:
            j = l2-1
            while j >= 0:
                k = i + j
                total = digit[k+1] + (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                print("\ni: ", i, "j: ", j, "k: ", k, "num1[i]:", num1[i], "num2[j]:", num2[j])
                print("total: ", total, "digit[k+1]:", digit[k+1], "digit[k]:", digit[k], " diigit:", digit, "\n")
                digit[k+1] = total%10
                digit[k] += total//10
                j -= 1
                print("after: digit: ", digit)
            i -= 1
        ans = ""
        print("digit: ", digit)
        for i in digit:
            if len(ans) == 0 and i == 0:
                continue
            ans += str(i)
        return ans
            
            
obj = Solution()
num1 = "123"
num2 = "789"
print(obj.multiply(num1, num2))

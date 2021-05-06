class Solution:
    def smallestFactorization(self, a):
        if a < 2:
            return a
        res = 0
        mul = 1
        for i in range(9, 1, -1):
            print("i is: ", i)
            while a%i == 0:
                a = int(a/i)
                res = mul*i + res 
                mul *= 10
                print("res: ", res, "mul: ", mul, "a: \n", a)
                
        return (res) if a < 2 else 0

obj = Solution()
print(obj.smallestFactorization(48))
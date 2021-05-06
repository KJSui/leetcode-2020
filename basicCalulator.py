class Solution:
    def calculate(self, s):
        stack = []
        res = 0
        i = 0
        operand = 0
        sign = 1

        for c in s:
            if c.isdigit():
                operand = operand * 10 + int(c)
            elif c is "+":
                res += operand * sign
                sign = 1
                operand = 0

            elif c is "-":
                res += operand * sign
                sign = -1
                operand = 0

            elif c is "(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0

            elif c is ")":
                res += sign * operand
                res *= stack.pop()
                res += stack.pop()
                operand = 0
        return res + sign * operand
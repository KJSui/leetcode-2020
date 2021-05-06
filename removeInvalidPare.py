class Solution:
    def __init__(self):
        self.valid_expressions = None
        self.min_removed = None

    def reset(self):
        self.valid_expressions = set()
        self.min_removed = float("inf")

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.reset()
        self.remaining(s, 0, 0, 0, 0, [])
        return list(self.valid_expressions)

    def remaining(self, s, left_count, right_count, index, remove_count, expr):
        if index == len(s):
            if left_count == right_count:
                if remove_count <= self.min_removed:
                    possible = "".join(expr)
                    if remove_count < self.min_removed:
                        self.min_removed = remove_count
                        self.valid_expressions = set()
                    self.valid_expressions.add(possible)
        else:
            curr = s[index]
            if curr != "(" and curr != ")":
                expr.append(curr)
                self.remaining(s, left_count, right_count, index+1, remove_count, expr)
                expr.pop()
            else:
                self.remaining(s, left_count, right_count, index+1, remove_count+1, expr)

                expr.append(curr)
                if curr == "(":
                    self.remaining(s, left_count+1, right_count, index+1, remove_count, expr)
                elif left_count > right_count:
                    self.remaining(s, left_count, right_count+1, index+1, remove_count, expr)
                expr.pop()




def dfs(string, index, left, right, res, minres, expr):
    if len(string) == index:
        if left == right:
            if minres <= self.minval:
                possible = "".join(expr)
                if minres < self.minval:
                    res = set()
                    self.minval = minres

                res.add(possible)

                return 

    curr = string[index]
    if curr != "(" or curr != ")":
        dfs(string, index+1, left, right, res, minres, expr+curr)

    else:
        dfs(string, index+1, left, right, res, minres+1, expr)
        if curr == "(":
            dfs(string, index+1, left+1, right, res, minres, expr+curr)
        else:
            dfs(string, index+1, left, right+1, res, minres, expr+curr)

        
        

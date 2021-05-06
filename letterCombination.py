class Solution:
    def letterCombination(self, digits):
        if len(digits) == 0:
            return []

        self.res = []
        self.backtrack("", digits)
        return self.res

    def backtrack(self, combinations, d):
        if len(digits) == 0:
            res.append(combinations)
            return
        for letter in digits[d[0]]:
            self.backtrack(combinations+letter, digits[1:])
        

    
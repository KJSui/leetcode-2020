class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse():
            N = len(formula)
            mp = collections.Counter()
            while self.i < N and formula[self.i] != ')':
                if (formula[self.i] == '('):
                    self.i += 1
                    for name, v in parse().items():
                        mp[name] += v 
                else:
                    i_start = self.i 
                    self.i += 1
                    while self.i < N and formula[self.i].islower():
                        self.i += 1
                    name = formula[i_start:self.i]
                    i_start = self.i 
                    while self.i < N and formula[self.i].isdigit():
                        self.i += 1
                    count[name] += int(formula[i_start:self.i] or 1)
            self.i += 1
            i_start = self.i 
            while self.i < N and formula[self.i].isdigit():
                self.i += 1
            if i_start < self.i:
                multi = int(formula[i_start:self.i])
                for name in count:
                    mp[name] *= multi
            return mp
        self.i = 0
        ans = []
        count = parse()
        for name in sorted(count):
            ans.append(name)
            multi = count[name]
            if multi > 1:
                ans.append(str(multi))
        return "".join(ans)
                
                
obj = Solution()
formula = "K4(ON(SO3)2)2"
print(obj.countOfAtoms(formula))

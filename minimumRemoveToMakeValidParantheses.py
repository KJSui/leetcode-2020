class Solution:
    def minRemoveToMakeValid(self, s):
        def delete_invalid_closing(string, open_symbol, close_symbol):
            sb = []
            balance = 0
            for i in string:
                if i == open_symbol:
                    balance += 1
                else:
                    if balance == 0:
                        continue
                    balance -= 1
                sb.append(i)

            return "".join(sb)
        s = delete_invalid_closing(s, '(', ')')
        s = delete_invalid_closing(s[::-1], ')', '(')
        return s[::-1]
        

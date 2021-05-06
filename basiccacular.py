class Solution:
    def calculate(self, s):
        stack = []
        signs = []
        t1 =0
        t2 =0
        i = 0
        c = 0
        while i < len(s):
            print("s[i]:", s[i], "i:", i)
            if ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
                c = i+1
                #print("c value: ", c, "s[c]: ", s[c])
                while c < len(s) and ord(s[c]) >= ord('0') and ord(s[c]) <= ord('9'):
                    print("s[c]: ", s[c])
                    c += 1
                if len(signs) > 0 and signs[-1] in ["/", "*"]:
                    if signs[-1] is "*":
                        tmp = int(stack.pop()) * int(s[i:c])
                    else:
                        tmp = int(int(stack.pop()) / int(s[i:c]))
                    stack.append(tmp)
                    signs.pop()
                else:
                    stack.append(s[i:c])

                i = c
                    
            elif s[i] is ")":
                sign = signs.pop()
                while sign is not '(':
                    print("sign (: stack: ", stack, " sign: ", signs)
                    t1 = int(stack.pop())
                    t2 = int(stack.pop())
                    
                    if sign is "+":
                        t1 = t1 + t2
                    elif sign is "-":
                        t1 = t2 - t1
                    else:
                        stack.append(t2)
                    stack.append(t1)
                    sign = signs.pop()
    
                if len(signs) > 0 and signs[-1] is "*":
                    t1 = stack.pop()
                    t2 = stack.pop()
                    t1 = int(t2) * int(t1) 
                    ##stack.append(t1)
                    signs.pop()
                    stack.append(t1)
                elif len(signs) > 0 and signs[-1] is "/":
                    t1 = stack.pop()
                    t2 = stack.pop()
                    t1 = int(int(t2)/int(t1))
                    signs.pop()
                    stack.append(t1)


                i += 1
            elif s[i] is " ":
                i += 1
                
            else:
                signs.append(s[i])
                i += 1
            print("stack: ", stack)
            print("signs: ", signs)    

        while len(stack) > 1:
            t1 = int(stack.pop())
            t2 = int(stack.pop())
            sign = signs.pop()
            if sign is "+":
                t1 = t1 + t2
            else:
                t1 = t2 - t1
            stack.append(t1)
            
        return stack.pop()
            
                
obj = Solution()
s = " 2-1 + 2 "
print(obj.calculate(s))
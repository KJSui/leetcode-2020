class Solution:
    def lonngest(self, str):
        st = set()
        leftbound = 0
        res = 0
        tmpl = 0
        for i in range(len(str)):
            if str[i] not st:
                st.add(str[i])
                tmpl += 1
                
            else:
                while leftbound < i and str[leftbound] != str[i]:
                    st.remove(str[leftbound])
                    leftbound += 1
                leftbound += 1
                tmpl = len(st)

            res = max(res, tmpl)

        return res 


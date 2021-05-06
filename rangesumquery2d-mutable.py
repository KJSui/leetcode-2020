class Node():
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.total = 0
        self.left = None
        self.right = None

class NumMatrix(object):
    def __init__(self, matrix):
        def construct(l, r, arr):
            if l > r:
                return
            if l == r:
                n = Node(l, r)
                n.total = arr[l]
            else:
                mid = (l + r)//2
                n = Node(l, r)
                left =  construct(l, mid, arr)
                right = construct(mid+1, r, arr)
                n.left = left
                n.right = right
                n.total = left.total + right.total

            return n

        self.st = []
        for i in range(len(matrix)):
            self.st.append(construct(0, len(matrix[0])-1, matrix[i]))

    
    def update(slef, row, col, val):
        def update_st(i, st):
            if st.l == st.r:
                st.total = val
                return
            mid = (st.l + st.r)//2
            if i <= mid:
                update_st(i, st.left)
            else:
                update_st(i, st.right)
            st.total = st.left.total + st.right.total
            return

        st_i = self.st[row]
        update_st(col, st_i)
        self.st[row] = st_i

    def sumRegion(self, row1, col1, row2, col2):
        
        def get_st_sum(c1, c2, st):
            if c1 == st.l and c2 == st.r:
                return st.total
            if c1 > st.r or c2 < st.l:
                return 0
            else:
                mid = (st.l + st.r)//2
                if c2 <= mid:
                    return get_st_sum(c1, c2, st.left)
                elif c1 > mid:
                    return get_st_sum(c1, c2, st.right)
                else:
                    left = get_st_sum(c1, mid, st.left)
                    right = get_st_sum(mid+1, c2, st.right)
                return left + right
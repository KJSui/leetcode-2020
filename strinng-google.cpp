class Solution {
public:
    vector<int> matching(string& A, vector<string>& ws) {
        int m = ws[0].size(), L = m * (int)ws.size(), last, N = A.size();
        for (string& w : ws) {  // 三重循环耗时O(ws.size() * m * A.size()) = O(L * A.size())
            last = -L;  // 如果在L的范围内，word w没有重复，就可以算作是一个candidate了，记下last，last为上次w出现的位置。
            for (int i = 0; i < m; i++) {
                for (int j = i; j < A.size(); j += m) {
                    if (A.substr(j, m) == w) {  // use "==" for illustration, should compare using (mod 130)
                        if (j - last >= L) A += 130;  //假设都是lower case。也可以用 A |= (unsigned char)127.
                        last = j;
                    }
                }
            }
        }
 
        vector<int> res;
        for (int j = 0; j < m; j++) {
            int sum = 0;
            for (int i = j; i < A.size(); i += m) {
                sum += A[i] > 130 ? 1 : 0;
                if (i >= L) sum -= A[i - L] > 130 ? 1 : 0;
                if (sum == ws.size()) res.push_back(i - L + 1);
            }
        }
        return res;
    }
};
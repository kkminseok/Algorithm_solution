**c++**

```c++
class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        int** DP = new int*[A.size()+1];
        for(int i = 0 ; i <A.size()+1;++i)
            DP[i] = new int[B.size()+1];
        int res = 0;
        for(int i = 0 ; i <A.size()+1;++i)
        {
            for(int j = 0 ; j <B.size()+1;++j)
            {
                if(i ==0 || j ==0) DP[i][j] =0;
                else
                {
                    if(A[i-1] == B[j-1]) DP[i][j] = DP[i-1][j-1] + 1;
                    else
                        DP[i][j] =0;
                    res = max(res,DP[i][j]);
                }
            }
        }
        
        return res;
    }
};
```
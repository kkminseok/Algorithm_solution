**c++**

```c++
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int DP[301][301]={0,};
        int h = matrix.size();
        int w = matrix[0].size();
        int result= 0;
        for(int i =0;i<h;++i){
            for(int j =0;j<w;++j){
                if(i==0 || j==0 || matrix[i][j]=='0')
                    DP[i][j] = matrix[i][j]-48;
                else
                {
                    DP[i][j] = min(DP[i-1][j-1],min(DP[i-1][j],DP[i][j-1])) +1;
                }
                result= max(result,DP[i][j]);
            }
        }
        return result*result;
        
    }
};
```
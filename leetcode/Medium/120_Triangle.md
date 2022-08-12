**c++**

```c++
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        if(triangle.size() == 1) return triangle[0][0];
        int res = INT_MAX;
        int DP[201][201]={0,};
        DP[0][0] = triangle[0][0];
        for(int i = 1 ;i<triangle.size();++i){
            for(int j = 0; j<= i;++j){
                
                if(j ==0){
                    DP[i][j] = DP[i-1][j] + triangle[i][j];
                }
                else if(j==i){
                    DP[i][j] = DP[i-1][j-1] + triangle[i][j];
                }
                else{
                    DP[i][j] = min(DP[i-1][j-1],DP[i-1][j]) + triangle[i][j];
                }
                if(i == triangle.size()-1){
                    res = min(res,DP[i][j]);
                }
            }
            
        }
        return res;
    }
};
```
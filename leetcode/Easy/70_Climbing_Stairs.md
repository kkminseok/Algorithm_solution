```c++
class Solution {
public:
    int climbStairs(int n) {
        int DP[46]={0,};
        if(n==1)
            return 1;
        DP[0]=1;
        DP[1]=1;
        for(int i=2;i<=n;++i)
        {
            DP[i]= DP[i-2] + DP[i-1];
        }
        return DP[n];
    }
};
```
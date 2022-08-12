**c++**

```c++
class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> DP(num+1);
        DP[0] = 0 ;
        if(num ==0)
            return DP;
        DP[1] = 1;
        int Two_exp = 1;
        for(int i = 1;i<=num;++i)
        {
            if(i == pow(2,Two_exp))
            {
                DP[i] = 1;
                ++Two_exp;
            }
            else
            {
                int pownum = pow(2,Two_exp-1);
                DP[i] = DP[pownum] + DP[i-pownum];
            }
        }
        
        return DP;
    }
};
```
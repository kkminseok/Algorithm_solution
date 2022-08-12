**c++**

```c++
class Solution {
public:
    int countPrimes(int n) {
        //에라토스테네스의 체
        if(n==0 || n==1)
            return 0;
        int* dp = new int[n+1];
        int res = 0;
        dp[0] = 0;
        dp[1] =0;
        
        for(int i = 2 ; i< n+1;++i)
            dp[i] = i;
        
        for(int i = 2; i<sqrt(n+1); ++i){
            if(dp[i] == 0) continue;
            for(int j = i*2 ; j<n+1 ; j +=i)
                dp[j]=0;
        }
        for(int i = 2;i<n;++i)
                if(dp[i]!=0) ++res;
        return res;
    }
};
```
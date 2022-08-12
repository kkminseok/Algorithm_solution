**c++**

```c++
class Solution {
public:
    int exp(int n){
        int i = 2;
        while(!(pow(i,2)<= n && pow(i+1,2)>n)){
            ++i;
        }
        return i;
    }
    int numSquares(int n) {
        vector<int> DP(n+4,987);
        DP[1]=1;
        DP[2]=2;
        DP[3]=3;
        if(n<=3)return DP[n];
        for(int i = 4 ;i<=n;++i){
            //거듭제곱 지수 찾기
            int findexp = exp(i);
            if(pow(findexp,2)==i) DP[i] = 1;
            else{
                while(findexp>1)
                {
                    int expr = pow(findexp,2);
                    DP[i] = min(DP[expr] + DP[i - expr], DP[i]);
                    --findexp;
                }
            }
        }
        return DP[n];
    }
};
```
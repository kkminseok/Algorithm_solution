**c++**

```c++
class Solution {
public:
    int minOperations(int n) {
        int* DP = new int[n+1];
        DP[0] =0;
        DP[1] = 0;
        for(int i =2;i<=n;++i)
            DP[i] = DP[i-2] + i-1;
        return DP[n];
    }
};
```
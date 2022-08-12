**c++**

```c++
class Solution {
public:
    int DP[31] = {};
    int fib(int n) {
        if(n==0) return 0;
        if(n==1) return 1;
        if(DP[n]!=0) return DP[n];
        return DP[n] = fib(n-1) + fib(n-2);
    }
};
```
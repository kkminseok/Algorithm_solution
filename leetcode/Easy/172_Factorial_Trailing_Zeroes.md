**c++**

```c++
class Solution {
public:
    int trailingZeroes(int n) {
        long long i = 5;
        int result = 0;
        for(i; n/i>0; i*=5)
            result += n/i;
        return result;
    }
};
```
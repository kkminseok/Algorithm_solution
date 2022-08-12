**c++**

```c++
class Solution {
public:
    bool reorderedPowerOf2(int N) {
        long long result = change(N);
        for(int i = 0;i<=31;++i)
        {
            if(result == change(1<<i)) return true;
        }
        return false;
        
    }
    long long change(int n){
        //2진수로 바꿔버림.
        long long result = 0;
        for(;n;n/=10) result += pow(10,n%10);
        return result;
    }
};


```
**c++**

```c++
class Solution {
public:
    long long cal(long long happy){
        long long res=0;
        while(happy!=0){
            res += pow(happy%10,2);
            happy/=10;
        }
        return res;
    }
    
    bool isHappy(int n) {
        long long happy = n;
        long long fasthappy = n;
        do{
            happy = cal(happy);
            fasthappy = cal(fasthappy);
            fasthappy = cal(fasthappy);
        }while(happy != fasthappy);
        return happy == 1 ? true : false;
    }
};
```
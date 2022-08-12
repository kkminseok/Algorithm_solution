**c++**

```c++
class Solution {
public:
    vector<int> constructArray(int n, int k) {
        vector<int> res(n,0);
        for(int i = 1 ; i< n+1;++i)
            res[i-1] = i;
        for(int i = 1 ; i < k ;++i){
            int left = i;
            int right= n-1;
            while(left<right){
                swap(res[left++],res[right--]);
            }
        }
        return res;
    }
};
```
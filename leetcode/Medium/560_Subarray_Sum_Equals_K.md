**c++**

```c++
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> um;
        um[0] ++;
        int res = 0 ;
        int sum = 0;
        for(int i = 0 ; i < nums.size();++i){
            sum += nums[i];
            res += um[sum-k];
            um[sum] ++;
        }
        return res;
    }
};
```
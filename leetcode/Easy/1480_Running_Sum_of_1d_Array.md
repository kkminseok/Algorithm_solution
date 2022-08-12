**c++**

```c++
class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> DP(nums.size(),0);
        DP[0] = nums[0];
        for(int i = 1 ; i < nums.size();++i)
            DP[i] =DP[i-1] + nums[i];
        return DP;
    }
};
```
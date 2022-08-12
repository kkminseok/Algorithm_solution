**c++**

```c++
class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size()==1)
            return nums[0];
        if(nums.size()==2)
            return max(nums[0],nums[1]);
        int* DP = new int[nums.size()];
        DP[0] = nums[0];
        DP[1] = nums[1];
        DP[2] = nums[2] + DP[0];
        int result = max(DP[2],DP[1]);
        for(size_t i = 3; i<nums.size();++i)
        {
            DP[i] = max(DP[i-2],DP[i-3]) + nums[i];
            result = max(result,DP[i]);
        }
        for(size_t i = 0;i<nums.size();++i)
            cout<<DP[i]<<" ";
        cout<<'\n';
        
        return result;
    }
};
```
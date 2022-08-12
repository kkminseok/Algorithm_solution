```c++
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if(nums.size()==1)
            return nums[0];
        int* DP = new int[nums.size()+1];
        DP[0] = nums[0];
        int result = DP[0];
        for(size_t i =1;i<nums.size();++i)
        {
            DP[i] = max(DP[i-1] + nums[i], nums[i]);
            result = max(result,DP[i]);
        }
        return result;
    }
};
```
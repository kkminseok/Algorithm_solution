**c++**

```c++
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int* DP =new int[nums.size()];
        for(int i =0 ;i<nums.size();++i)
            DP[i] = 1;
        int result = 1;
        for(int i = 1; i<nums.size();++i)
        {
            for(int j =0;j<i;++j)
            {
                if(nums[i]> nums[j])
                    DP[i] = max(DP[i],DP[j]+1);
                result = max(result,DP[i]);
            }
        }
        return result;
    }
};
```
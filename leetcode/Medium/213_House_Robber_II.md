**c++**

```c++
class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size()==1)
            return nums[0];
        //DP를 2개만듦
        //DP는 첫 번째 집을 들르는 경우
        //DP2는 두 번째 집을 들르는 경우
        int* DP = new int[nums.size()];
        int* DP2 = new int[nums.size()];
        DP[0] = nums[0];
        DP[1] = nums[0];
        
        DP2[0] = 0;
        DP2[1]=nums[1];
        
        for(size_t i =2;i<nums.size();++i)
        {
            if(i !=nums.size()-1)
            {
                DP[i] = max(DP[i-2] + nums[i], DP[i-1]);
            }
            DP2[i] = max(DP2[i-2]+nums[i],DP2[i-1]);
        }
        int result = max(DP[nums.size()-2],DP2[nums.size()-1]);
        
        return result;
    }
};
```
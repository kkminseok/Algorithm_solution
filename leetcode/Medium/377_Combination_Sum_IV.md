**c++**

```c++
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        unsigned int* DP = new unsigned int[sizeof(int) * (target+1)];
        memset(DP,false,sizeof(int) * (target+1));
        DP[0]= 1;
        for(int i =1;i<=target; ++i)
        {
            for(int j =0;j<nums.size();++j)
            {
                if(i >= nums[j])
                {
                    DP[i] += DP[i-nums[j]];
                }
            }
        }
        
        return DP[target];
    }
};


/*
        int combinationSum4(vector<int>& nums, int target) {
        vector<unsigned int> result(target + 1);
        result[0] = 1;
        for (int i = 1; i <= target; ++i) {
            for (int x : nums) {
                if (i >= x) result[i] += result[i - x];
            }
        }
        
        return result[target];
    }
*/


```
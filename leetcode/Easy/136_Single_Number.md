```c++
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int result = 0;
        for(size_t i = 0; i<nums.size();i+=2)
        {
            if(i ==nums.size()-1|| nums[i] != nums[i+1])
            {
                result = nums[i];
                break;
            }
        }
        return result;
    }
};
```
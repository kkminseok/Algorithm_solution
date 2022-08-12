```c++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int left =0;
        for(size_t i=0;i<nums.size();++i)
        {
            nums[left++] = nums[i];
            while(i+1< nums.size() && nums[i] == nums[i+1])
            {
                ++i;
            }
        }
        return left;
    }
};
```

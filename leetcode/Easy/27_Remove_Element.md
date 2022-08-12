```c++
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int left =0;
        for(size_t i =0;i<nums.size();++i)
        {
            if(nums[i]==val)
                continue;
            else
            {
                nums[left++] =nums[i];
            }
        }
        return left;
        
    }
};
```

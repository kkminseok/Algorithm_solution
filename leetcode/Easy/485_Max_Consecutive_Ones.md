```c++
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int countz = 0;
        int result =0;
        if(nums.size()==1 &&nums[0]==0)
            return 0;
        for(size_t i=0;i<nums.size();++i)
        {
            if(nums[i]==0)
                countz=0;
            else if(nums[i]==1)
            {
                countz++;
            }
            if(result<countz)
                result =countz;

        }
        return result;
    }
 
};
```

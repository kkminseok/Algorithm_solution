**python**


```pyhton
class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums)-1) : 
            if nums[i] > nums[i+1] : 
                return nums[i+1]
        return nums[0]
```     

-----  

**c++**

```c++

class Solution {
public:
    int findMin(vector<int>& nums) {
        for(size_t i= 0;i<nums.size()-1;++i)
        {
            if(nums[i] >nums[i+1])
                return nums[i+1];
        }
        return nums[0];
        
    }
};
```
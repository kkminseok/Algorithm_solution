**c++**


```c++
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int major = nums[0];
        int count = 1;
        for(size_t i = 1;i<nums.size();++i)
        {
            if(count==0)
            {
                major = nums[i];
                ++count;
            }
            else if(nums[i]==major)
                ++count;
            else
                --count;
        }
        return major;
    }
};
```

-----  

**python**

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        major = nums[0]
        for i in range(1,len(nums)):
            if count == 0 :
                major = nums[i]
                count = 1
            elif nums[i] == major : 
                count += 1
            else : 
                count -= 1
        return major
```
**python**

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        i = 0
        while i < len(nums):
            if nums[i]<=0 :
                i+=1
                continue
            if count != nums[i]:
                return count
            while i< len(nums) and count == nums[i]:
                i+=1
            count+=1
        return count;
```

-----  

**c++**

```c++
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int count =1;
        for(size_t i =0;i<nums.size();)
        {
            if(nums[i]<=0)
            {
                ++i;
                continue;
            }
            if(count!=nums[i])
                return count;
            while(i<nums.size() && count==nums[i])
                ++i;
            count+=1;
        }
        return count;
    }
};
```
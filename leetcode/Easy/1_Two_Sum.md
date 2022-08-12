**c++**

```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        for(size_t i=0;i<nums.size();++i)
        {
            for(size_t j = i+1; j<nums.size();++j)
            {
                if(nums[i] + nums[j]==target)
                {
                    result.push_back(i);
                    result.push_back(j);
                    return result;
                }
            }
        }
        return result;
    }
};
```

-----  

**python**

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result
```
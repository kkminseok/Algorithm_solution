**python**

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0 
        if len(nums) == 1 : 
            return 0
        else : 
            for i in range(1,len(nums)):
                if nums[i] <= nums[i-1] : 
                    res += nums[i-1] - nums[i]+1
                    nums[i] = nums[i-1] + 1
        return res         
```
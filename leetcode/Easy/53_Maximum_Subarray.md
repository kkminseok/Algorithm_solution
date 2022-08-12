**python**

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res =nums[0]
        for i in range(1,len(nums)):
            nums[i] = max(nums[i-1]+nums[i],nums[i] )
            res = max(nums[i],res)
        return res
```
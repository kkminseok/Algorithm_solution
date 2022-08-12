**python**

```python
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        return (nums[size-1] * nums[size-2]) - (nums[0] * nums[1])
```
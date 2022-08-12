**python**

```python
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        l,r = -1,-1
        ans = 0
        for i in range(len(nums)):
            if nums[i] >right : 
                l = i
            if nums[i] >= left : 
                r = i
            ans+=r-l
        return ans
```
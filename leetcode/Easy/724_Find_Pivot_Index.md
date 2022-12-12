**python**

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum=0
        rightsum=sum(nums) - nums[0]
        if leftsum == rightsum:
                return 0
        for i in range(1,len(nums)):
            leftsum+=nums[i-1]
            rightsum-=nums[i]
            if leftsum == rightsum:
                return i
        return -1
```
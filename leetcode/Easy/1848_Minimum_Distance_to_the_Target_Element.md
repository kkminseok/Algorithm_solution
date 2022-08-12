**python**

```python
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = 987654321 
        for i in range(len(nums)):
            if nums[i] == target : 
                res = min(res, abs(start-i))
        return res
```
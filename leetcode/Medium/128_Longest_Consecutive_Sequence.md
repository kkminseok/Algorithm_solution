**python**

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        res = 0 
        count = 1
        print(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i]+1 == nums[i+1] : 
                count+=1 
            else :
                res = max(res,count)
                count=1
        return max(res,count)
```
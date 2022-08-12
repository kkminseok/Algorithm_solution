**python**

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        size = len(nums)
        k = k%size
        tempres = copy.deepcopy(nums)
        print(tempres)
        for i in range(size):
            rotate = (i+k) %size
            nums[rotate] = tempres[i]
    # dicuss 코드            
    def rotate2(self, nums, k):
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
        
        
        
```
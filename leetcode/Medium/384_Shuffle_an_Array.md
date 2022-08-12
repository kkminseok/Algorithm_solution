**python**

```python
class Solution:
    
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums
        """
        Resets the array to its original configuration and return it.
        """
        

    def shuffle(self) -> List[int]:
        ans = self.nums[:]                     # copy list
        for i in range(len(ans)-1, 0, -1):     # start from end
            j = random.randrange(0, i+1)    # generate random index 
            ans[i], ans[j] = ans[j], ans[i]    # swap
        return ans
        """
        Returns a random shuffling of the array.
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
```

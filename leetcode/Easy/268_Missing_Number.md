**c++**
```c++
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        for(int i =0;i<nums.size();++i)
            if(nums[i] != i)
                return i;
        return nums[nums.size()-1]+1;
    }
};
```

**python**

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
            nums.sort()
            for i in range (0,len(nums)):
                if nums[i] != i :
                    return i
            return nums[len(nums)-1]+1;

```
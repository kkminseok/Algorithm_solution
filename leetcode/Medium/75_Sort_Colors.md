**python**

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        ns = len(nums)
        countz = [0] * 3
        for i in range(ns):
            countz[nums[i]]+=1
        index = 0
        for i in range(ns):
            while index < 3 and countz[index]==0:
                index+=1
            nums[i] = index
            countz[index]-=1
```

----- 

**c++**

```c++   
class Solution {
public:
    void sortColors(vector<int>& nums) {
     int ns = nums.size();
     int countz[3] = {0,0,0};    
     for(size_t i =0;i<ns;++i)
     {
         countz[nums[i]]++;
     }
    int index =0;
    for(size_t i =0 ;i<ns;++i)
    {
        while(index<3 && countz[index]==0)
            ++index;
        nums[i] = index;
        countz[index]--;

    }
    }
};
```
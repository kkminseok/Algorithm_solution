**python**

```python

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in range(len(nums)) : 
            temp = dic.get(nums[i],2)
            if temp != 2 :
                return True
            dic[nums[i]] = 1
        return False
```

-----  

**c++**

```c++

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int,bool> map;
        for(size_t i = 0;i<nums.size();++i)
        {
            if(map[nums[i]]==true)
                return true;
            map[nums[i]]=true;
        }
        return false;
    }
};

```
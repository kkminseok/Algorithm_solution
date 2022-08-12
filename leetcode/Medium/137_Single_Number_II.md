**python**

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #하나 빼고 전부 3번 반복될 때 나머지 1개
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic : 
                dic[nums[i]]=1
            else : 
                dic[nums[i]]+=1
                if dic[nums[i]] == 3 :
                    del[dic[nums[i]]]
        res = list(dic.keys())
        return res[0]
```
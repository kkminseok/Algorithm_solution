**python**

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(numbers)):
            if target - numbers[i] in dic : 
                return [dic[target - numbers[i]],i+1]
            
            else:
                dic[numbers[i]] = i+1
```
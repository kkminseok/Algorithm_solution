**python**

```python
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dic = {}
        pivot = 0
        for i in range(len(s)):
            if s[i] not in dic : 
                dic[s[i]]=1
            else : 
                dic[s[i]]+=1
            pivot = dic[s[i]]
        for count in dic : 
            if dic[count] != pivot: 
                return False
        return True
```